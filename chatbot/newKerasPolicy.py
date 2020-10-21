from rasa.core.policies.keras_policy import KerasPolicy
from typing import Dict, Text, Any, List, Union, Optional, Tuple
import tensorflow as tf
from rasa.core.trackers import DialogueStateTracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Tracker
import ws_service
from rasa_sdk import ActionExecutionRejection

import uuid
import os
import logging
class newKerasPolicy(KerasPolicy):

    def model_architecture(self, input_shape: Tuple[int, int], output_shape: Tuple[int, Optional[int]]) -> tf.keras.models.Sequential :
        from tensorflow.keras.models import Sequential
        from tensorflow.keras.layers import (
        Masking,
        LSTM,
        Dense,
        TimeDistributed,
        Activation,
        )
        # Build Model
        model = Sequential()
        # the shape of the y vector of the labels,
        # determines which output from rnn will be used
        # to calculate the loss
        if len(output_shape) == 1:
            # y is (num examples, num features) so
            # only the last output from the rnn is used to
            # calculate the loss
            model.add(Masking(mask_value=-1, input_shape=input_shape))
            model.add(LSTM(self.rnn_size, dropout=0.2))
            model.add(Dense(input_dim=self.rnn_size, units=output_shape[-1]))
        elif len(output_shape) == 2:
            # y is (num examples, max_dialogue_len, num features) so
            # all the outputs from the rnn are used to
            # calculate the loss, therefore a sequence is returned and
            # time distributed layer is used

            # the first value in input_shape is max dialogue_len,
            # it is set to None, to allow dynamic_rnn creation
            # during prediction
            model.add(Masking(mask_value=-1, input_shape=(None, input_shape[1])))
            model.add(LSTM(self.rnn_size, return_sequences=True, dropout=0.2))
            model.add(TimeDistributed(Dense(units=output_shape[-1])))
        
        else:
            raise ValueError(
                "Cannot construct the model because"
                "length of output_shape = {} "
                "should be 1 or 2."
                "".format(len(output_shape))
            )

        model.add(Activation("softmax"))

        model.compile(
            loss="categorical_crossentropy", optimizer="rmsprop", metrics=["accuracy"]
        )
        if common_utils.obtain_verbosity() > 0:
            model.summary()

        return model




    def train(self,training_trackers: List[DialogueStateTracker],domain : Dict[Text, Any],**kwargs: Any,) -> None :
        np.random.seed(self.random_seed)
        tf.random.set_seed(self.random_seed)

        training_data = self.featurize_for_training(training_trackers, domain, **kwargs)
        # noinspection PyPep8Naming
        shuffled_X, shuffled_y = training_data.shuffled_X_y()
        if self.model is None:
            self.model = self.model_architecture(
                shuffled_X.shape[1:], shuffled_y.shape[1:]
            )

        logger.debug(
            f"Fitting model with {training_data.num_examples()} total samples and a "
            f"validation split of {self.validation_split}."
        )
        # filter out kwargs that cannot be passed to fit
        self._train_params = self._get_valid_params(
            self.model.fit, **self._train_params
        )

        self.model.fit(
            shuffled_X,
            shuffled_y,
            epochs=self.epochs,
            batch_size=self.batch_size,
            shuffle=False,
            verbose=common_utils.obtain_verbosity(),
            **self._train_params,
        )
        self.current_epoch = self.epochs
        logger.debug("Done fitting Keras Policy model.")
        print("hello")

     