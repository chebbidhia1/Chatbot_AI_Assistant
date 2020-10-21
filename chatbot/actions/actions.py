from typing import Dict, Text, Any, List, Union, Optional, Tuple

from rasa_sdk import ActionExecutionRejection
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT, EventType

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import ws_service

import uuid
import os
import logging

logger = logging.getLogger(__name__)
              

class CreateTaskForm(FormAction):
    """Example of a custom form action
    create_task_form contains the logic to loop over the required slots and ask the user for this information.
    """

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "create_task_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        SlotSet("stream_id", tracker.slots['stream_id'])
        print("from required slots create task form")
        print(tracker.slots['stream_id'])
        #when the form create_task_form is activated we will move to the templates and search for utter_ask with the slot on question
        # if it's filled it will move to the next slot it will move to the next slot
        return ["org_id", "ws_id", "stream_id", "task_name", "task_priority"]


    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {"name": self.from_entity(entity="name", intent=["inform"]),
                "org_id": self.from_entity(entity="org_id", intent=["inform"]),
                "ws_id": self.from_entity(entity="ws_id", intent=["inform"]),
                "stream_id": self.from_entity(entity="stream_id", intent=["inform"]),
                "task_name": self.from_entity(entity="task_name", intent=["inform"]),
                "task_priority": self.from_entity(entity="task_priority", intent=["inform"]),
                }

    @staticmethod
    def task_priority_db():
        # type: () -> List[Text]
        """Database of supported task_priority"""
        return ["0","10","20","30"]

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""

        try:
            int(string)
            return True
        except ValueError:
            return False
            

    @staticmethod
    def get_token():
        # events = tracker.current_state()['events']
        # user_events = []
        # for e in events:
        #     if e['event'] == 'user':
        #         user_events.append(e)
                
        # token = user_events[-1]['metadata']
        # print("nada token : ", token)
        return "eyJhbGciOiJSUzI1NiIsImtpZCI6IjM0ZjcxYTRlOTU0NTk0ZjYwM2UzOTZiN2UyNWRlNTliOTNlNjMyYjYifQ.eyJpc3MiOiJodHRwczovL3Nzby5kZXYubWVlcmFzcGFjZS5jb20iLCJzdWIiOiJDaVF3TkRRMk56ZGlOUzAyTjJaaUxUUTFOVGt0T0dNNVpDMWtPR1ZqWVRVM1lqQXhNREVTQld4dlkyRnMiLCJhdWQiOiJ3b3Jrc3BhY2UiLCJleHAiOjE1OTgwODYyMzMsImlhdCI6MTU5NzgyNzAzMywiYXRfaGFzaCI6ImprQlQyM3hJY1c2ZFp6RElZcEpNQVEiLCJlbWFpbCI6Imphc3Nlci5iZW5hYmRhbGxhaEB0YXJnZXQtZW5lcmd5c29sdXRpb25zLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYW1lIjoiSmFzc2VyIn0.hdWzJH2eQ4ib_fteTDBHAGp8sybuZ3YpVeoOcnlGVEbfwyPCoo82pn1GsPvv5AzHv7e2oJvKXzbocfiphV-xipuuc70DSZuKa_SSl_XyuZqTVg6MBUEqap1VDowvyBVLtqSXh6DNW3lumafE_KHbAzeHQRbva9Vk2tIomhIFWEvP1HKu0-k-EqYxkskdkhPIzuzQ9zO3YVLTDZGu-WeQxaTymq58RniW5JosfxLoehsiZO-_TSd4j4lhMdsn1bU3nlYXfaUTa_fSiXzpUW-cgIljR2XdKmAJhe8p16WyNPgYMBw179W3ek6Gvnwt5WLQ1eKGmuFmacqDGMvbhrwBng"

    def request_next_slot(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: Dict[Text, Any],
    ) -> Optional[List[EventType]]:
        """Request the next slot and utter template if needed,
            else return None"""

        intent = tracker.latest_message.get("intent", {}).get("name")
        if intent == 'deny':
            return self.deactivate()
        else :

            for slot in self.required_slots(tracker):
                if self._should_request_slot(tracker, slot):

                # Condition to validate org_id
                    if slot == "org_id": 

                        #print("token", self.get_token())

                    # fetch the data and store it in the format used by buttons.
                        org_list = ws_service.get_organisations(token=self.get_token())
                        if not org_list:
                            return [SlotSet(REQUESTED_SLOT, "0")]

                        dispatcher.utter_message(
                            template=f"utter_ask_{slot}", **tracker.slots, buttons=org_list
                        )

                        return [SlotSet(REQUESTED_SLOT, slot)]
                
                    # Condition to validate ws_id
                    elif slot == "ws_id":

                        # get org_id slot
                        org_id =  tracker.get_slot('org_id')

                        # fetch the data and store it in the format used by buttons.
                        ws_list, _ = ws_service.get_workspaces(token=self.get_token(),org_id=org_id)
                        print("*************")
                        print(ws_list)
                        print(type(ws_list))
                        if not ws_list:
                            dispatcher.utter_message(text="you don't have any workspace")
                            CreateWorkspaceForm()                        
                            # TODO: create new workspace
                            # OR return self._deactivate()
                            return [SlotSet(REQUESTED_SLOT, "0")]
                        ws_list.append({'title': 'i want to create workspace','payload':'/create_workspace' })
                        dispatcher.utter_message(
                            template=f"utter_ask_{slot}", **tracker.slots, buttons=ws_list
                        )

                        return [SlotSet(REQUESTED_SLOT, slot)]

                    # Condition to validate stream_id
                    elif slot == "stream_id":
                        if tracker.slots['stream_id'] ==  None :
                            print("noooooooooooone") 
                        # get org_id slot
                            org_id =  tracker.get_slot('org_id')

                        # fetch the streams and store them in the format used by buttons.
                            _ , streams = ws_service.get_workspaces(token=self.get_token(),org_id=org_id)

                            stream_list = streams.get(tracker.get_slot('ws_id'))
                            intent = tracker.latest_message.get("intent", {}).get("name")
                            if  not stream_list  :
                                dispatcher.utter_message(text="you don't have any stream")
                                dispatcher.utter_message(text="do you want to create a new stream")
                                CreateStreamForm()
                                return [SlotSet(REQUESTED_SLOT, "0")]
                            stream_list.append({'title': 'i want to create stream','payload':'/create_stream' })
                            dispatcher.utter_message(
                                template=f"utter_ask_{slot}", **tracker.slots, buttons=stream_list
                            )
                        # to do stream list exists but i want to add another stream
                            return [SlotSet(REQUESTED_SLOT, slot)]        

                    logger.debug(f"Request next slot '{slot}'")
                    dispatcher.utter_message(
                        template=f"utter_ask_{slot}", **tracker.slots
                    )

                    # if not followup validation
                    return [SlotSet(REQUESTED_SLOT, slot)]

                    
            # return None
    
    def validate(self,
                 dispatcher: CollectingDispatcher,
                 tracker: Tracker,
                 domain: Dict[Text, Any]) -> List[Dict]:
        """Validate extracted requested slot
            else reject the execution of the form action
        """
        #SlotSet("stream_id", tracker.slots['stream_id'])
        # extract other slots that were not requested
        # but set by corresponding entity
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)
        print("slot_values *****")
        print(slot_values)

        # extract requested slot
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher,
                                                           tracker, domain))

            print("#### slot_to_fill", slot_to_fill)
            print("#### slot_values", slot_values)

            if slot_to_fill == 'org_id' and not slot_values:
                print("###### tracker.latest_message.text",
                      (tracker.latest_message)['text'])
                # validation failed, set slot to user message
                slot_values['org_id'] = (tracker.latest_message)['text']

            elif slot_to_fill == 'ws_id' and not slot_values:
                print("###### tracker.latest_message.text",
                      (tracker.latest_message)['text'])

                # validation failed, set slot to user message
                intent = tracker.latest_message.get("intent", {}).get("name")
                # validation failed, set slot to user message
                print(intent + "from validation")
                if intent == "inform" :
                    slot_values['ws_id'] = (
                    tracker.latest_message)['text']
                else :
                    SlotSet(REQUESTED_SLOT, "0")

            elif slot_to_fill == 'stream_id' and not slot_values:

                print("###### tracker.latest_message.text",
                      (tracker.latest_message)['text'])
                intent = tracker.latest_message.get("intent", {}).get("name")
                # validation failed, set slot to user message
                print(intent + "from validation")
                if intent == "inform" :
                    slot_values['stream_id'] = (
                    tracker.latest_message)['text']
                else :
                    SlotSet(REQUESTED_SLOT, "0")
                

            elif slot_to_fill == 'task_name' and not slot_values:
                print("###### tracker.latest_message.text",
                      (tracker.latest_message)['text'])
                # validation failed, set slot to user message

                slot_values['task_name'] = (
                    tracker.latest_message)['text']        
            
            elif slot_to_fill == 'task_priority' and not slot_values:
                print("###### tracker.latest_message.text",
                      (tracker.latest_message)['text'])
                
                # validation failed, set slot to user message
                slot_values['task_priority'] = (
                    tracker.latest_message)['text'] 

            if not slot_values:
                # reject form action execution
                # if some slot was requested but nothing was extracted
                # it will allow other policies to predict another action
                raise ActionExecutionRejection(self.name(),
                                               "Failed to validate slot {0} "
                                               "with action {1}"
                                               "".format(slot_to_fill,
                                                         self.name()))
                

        # we'll check when validation failed in order
        # to add appropriate utterances
        for slot, value in slot_values.items():

            if slot == 'task_priority':
                if value not in self.task_priority_db():
                    dispatcher.utter_template('utter_wrong_task_priority', tracker)
                    # validation failed, set slot to None
                    slot_values[slot] = None


        # validation succeed, set the slots values to the extracted values
        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_template('utter_submit', tracker)
        dispatcher.utter_message("do you confirm task creation ?")

        return []  

class ActionCreateTask(Action):
    def name(self):
        """Unique identifier of the form"""
        return 'action_create_task'

    def run(self, dispatcher, tracker, domain):
        
        task_name = tracker.get_slot('task_name')
        print("task_name slot : ",task_name)

        stream_id = tracker.get_slot('stream_id')
        print("stream_id slot : ",stream_id)


        priority = tracker.get_slot('task_priority')
        print("priority slot: ",priority)
        
        # create the task with graphql
        task = ws_service.create_task(CreateTaskForm.get_token(),task_name,int(stream_id),int(priority))
        
        if task is not None:
            dispatcher.utter_message("task successfully created with name: {name} 🚀".format(name=task_name)) 

##########################################################################################
class CreateStreamForm(FormAction):
    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "create_stream_form"
    @staticmethod
    def get_token():
        return "eyJhbGciOiJSUzI1NiIsImtpZCI6IjM0ZjcxYTRlOTU0NTk0ZjYwM2UzOTZiN2UyNWRlNTliOTNlNjMyYjYifQ.eyJpc3MiOiJodHRwczovL3Nzby5kZXYubWVlcmFzcGFjZS5jb20iLCJzdWIiOiJDaVF3TkRRMk56ZGlOUzAyTjJaaUxUUTFOVGt0T0dNNVpDMWtPR1ZqWVRVM1lqQXhNREVTQld4dlkyRnMiLCJhdWQiOiJ3b3Jrc3BhY2UiLCJleHAiOjE1OTgwODYyMzMsImlhdCI6MTU5NzgyNzAzMywiYXRfaGFzaCI6ImprQlQyM3hJY1c2ZFp6RElZcEpNQVEiLCJlbWFpbCI6Imphc3Nlci5iZW5hYmRhbGxhaEB0YXJnZXQtZW5lcmd5c29sdXRpb25zLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYW1lIjoiSmFzc2VyIn0.hdWzJH2eQ4ib_fteTDBHAGp8sybuZ3YpVeoOcnlGVEbfwyPCoo82pn1GsPvv5AzHv7e2oJvKXzbocfiphV-xipuuc70DSZuKa_SSl_XyuZqTVg6MBUEqap1VDowvyBVLtqSXh6DNW3lumafE_KHbAzeHQRbva9Vk2tIomhIFWEvP1HKu0-k-EqYxkskdkhPIzuzQ9zO3YVLTDZGu-WeQxaTymq58RniW5JosfxLoehsiZO-_TSd4j4lhMdsn1bU3nlYXfaUTa_fSiXzpUW-cgIljR2XdKmAJhe8p16WyNPgYMBw179W3ek6Gvnwt5WLQ1eKGmuFmacqDGMvbhrwBng"
    
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        #when the form create_task_form is activated we will move to the templates and search for utter_ask with the slot on question
        # if it's filled it will move to the next slot it will move to the next slot
        return ["org_id","ws_id","stream_name"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {"org_id": self.from_entity(entity="org_id", intent=["inform"]),
                "ws_id": self.from_entity(entity="ws_id", intent=["inform"]),
                "stream_name": self.from_entity(entity="stream_name", intent=["inform"])
                }
    def request_next_slot(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: Dict[Text, Any],
    ) -> Optional[List[EventType]]:
        """Request the next slot and utter template if needed,
            else return None"""

        intent = tracker.latest_message.get("intent", {}).get("name")
        if intent == 'deny':
            return self.deactivate()
        else :

            for slot in self.required_slots(tracker):
                if self._should_request_slot(tracker, slot):

                # Condition to validate org_id
                    if slot == "org_id": 

                        #print("token", self.get_token())

                    # fetch the data and store it in the format used by buttons.
                        org_list = ws_service.get_organisations(token=self.get_token())
                        if not org_list:
                            return [SlotSet(REQUESTED_SLOT, "0")]

                        dispatcher.utter_message(
                            template=f"utter_ask_{slot}", **tracker.slots, buttons=org_list
                        )

                        return [SlotSet(REQUESTED_SLOT, slot)]

                    # Condition to validate ws_id
                    elif slot == "ws_id":

                        # get org_id slot
                        org_id =  tracker.get_slot('org_id')

                        # fetch the data and store it in the format used by buttons.
                        ws_list, _ = ws_service.get_workspaces(token=self.get_token(),org_id=org_id)
                        if not ws_list:
                            dispatcher.utter_message(text="you don't have any workspace")
                            # TODO: create new workspace
                            CreateWorkspaceForm()
                            return [SlotSet(REQUESTED_SLOT, "0")]
                        ws_list.append({'title': 'i want to create workspace','payload':'/create_workspace' })
                        dispatcher.utter_message(
                            template=f"utter_ask_{slot}", **tracker.slots, buttons=ws_list
                        )
                        return [SlotSet(REQUESTED_SLOT, slot)]

                    logger.debug(f"Request next slot '{slot}'")
                    dispatcher.utter_message(
                    template=f"utter_ask_{slot}", **tracker.slots
                    )
                    return [SlotSet(REQUESTED_SLOT, slot)]
    
    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_template('utter_submit', tracker)
        dispatcher.utter_message("do you confirm stream creation ?")
        return []
    
    def validate(self,
                 dispatcher: CollectingDispatcher,
                 tracker: Tracker,
                 domain: Dict[Text, Any]) -> List[Dict]:
        """Validate extracted requested slot
            else reject the execution of the form action
        """

        for slot_name in CreateTaskForm.required_slots(tracker):
            print(slot_name , tracker.get_slot(slot_name))
        # extract other slots that were not requested
        # but set by corresponding entity
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)

        # extract requested slot
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher,
                                                           tracker, domain))
            print("#### slot_to_fill", slot_to_fill)
            print("#### slot_values", slot_values)

            if slot_to_fill == 'org_id' and not slot_values:
                print("###### tracker.latest_message.text",
                      (tracker.latest_message)['text'])
                # validation failed, set slot to user message
                slot_values['org_id'] = (tracker.latest_message)['text']

            elif slot_to_fill == 'ws_id' and not slot_values:
                print("###### tracker.latest_message.text",
                      (tracker.latest_message)['text'])
                # validation failed, set slot to user message

                intent = tracker.latest_message.get("intent", {}).get("name")
                # validation failed, set slot to user message
                print(intent + "from validation")
                if intent == "inform" :
                    slot_values['ws_id'] = (
                    tracker.latest_message)['text']
                else :
                    SlotSet(REQUESTED_SLOT, "0")

            elif slot_to_fill == 'stream_name' and not slot_values:
                print("###### tracker.latest_message.text",
                      (tracker.latest_message)['text'])
                # validation failed, set slot to user message
                slot_values['stream_name'] = (
                    tracker.latest_message)['text']         

            if not slot_values:
                print("********** validation failed")
                # reject form action execution
                # if some slot was requested but nothing was extracted
                # it will allow other policies to predict another action
                raise ActionExecutionRejection(self.name(),
                                               "Failed to validate slot {0} "
                                               "with action {1}"
                                               "".format(slot_to_fill,
                                                         self.name()))
        # validation succeed, set the slots values to the extracted values
        return [SlotSet(slot, value) for slot, value in slot_values.items()]


        
class ActionCreateStream(Action):
    def name(self):
        """Unique identifier of the form"""
        return 'action_create_stream'

    def run(self, dispatcher, tracker, domain):
        
        stream_name = tracker.get_slot('stream_name')
        print("stream_name slot : ",stream_name)

        ws_id = tracker.get_slot('ws_id')
        print("ws_id slot : ",ws_id)

        
        # create the stream with graphql
        print("************************* into action create stream ************************************** ")
        stream = ws_service.create_stream(CreateStreamForm().get_token(),stream_name,int(ws_id) )
         
        if stream is not None:
            dispatcher.utter_message("stream successfully created with name: {name} 🚀".format(name=stream_name))
            tracker.slots['stream_id'] = stream.get('id')
            print(tracker.slots['stream_id'])
            SlotSet("stream_id", tracker.slots['stream_id'])
            print("*****************collect values of required slots filled before activation")
        # collect values of required slots filled before activation
        

        else :
            print("erorr in graphql *****************") 

        for slot_name in CreateTaskForm.required_slots(tracker):
            
            print(slot_name , tracker.get_slot(slot_name))   
        return [SlotSet("stream_id", tracker.slots['stream_id'])]    

        
           
########################################################################################################


class CreateWorkspaceForm(FormAction):
    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "create_workspace_form"
    @staticmethod
    def get_token():
        return "eyJhbGciOiJSUzI1NiIsImtpZCI6IjM0ZjcxYTRlOTU0NTk0ZjYwM2UzOTZiN2UyNWRlNTliOTNlNjMyYjYifQ.eyJpc3MiOiJodHRwczovL3Nzby5kZXYubWVlcmFzcGFjZS5jb20iLCJzdWIiOiJDaVF3TkRRMk56ZGlOUzAyTjJaaUxUUTFOVGt0T0dNNVpDMWtPR1ZqWVRVM1lqQXhNREVTQld4dlkyRnMiLCJhdWQiOiJ3b3Jrc3BhY2UiLCJleHAiOjE1OTgwODYyMzMsImlhdCI6MTU5NzgyNzAzMywiYXRfaGFzaCI6ImprQlQyM3hJY1c2ZFp6RElZcEpNQVEiLCJlbWFpbCI6Imphc3Nlci5iZW5hYmRhbGxhaEB0YXJnZXQtZW5lcmd5c29sdXRpb25zLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYW1lIjoiSmFzc2VyIn0.hdWzJH2eQ4ib_fteTDBHAGp8sybuZ3YpVeoOcnlGVEbfwyPCoo82pn1GsPvv5AzHv7e2oJvKXzbocfiphV-xipuuc70DSZuKa_SSl_XyuZqTVg6MBUEqap1VDowvyBVLtqSXh6DNW3lumafE_KHbAzeHQRbva9Vk2tIomhIFWEvP1HKu0-k-EqYxkskdkhPIzuzQ9zO3YVLTDZGu-WeQxaTymq58RniW5JosfxLoehsiZO-_TSd4j4lhMdsn1bU3nlYXfaUTa_fSiXzpUW-cgIljR2XdKmAJhe8p16WyNPgYMBw179W3ek6Gvnwt5WLQ1eKGmuFmacqDGMvbhrwBng"
    
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        #when the form create_task_form is activated we will move to the templates and search for utter_ask with the slot on question
        # if it's filled it will move to the next slot it will move to the next slot
        return ["org_id","workspace_type","workspace_name","workspace_description"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {"org_id": self.from_entity(entity="org_id", intent=["inform"]),
                "workspace_type": self.from_entity(entity="workspace_type", intent=["inform"]),
                "workspace_name": self.from_entity(entity="workspace_name", intent=["inform"]),
                "workspace_description": self.from_entity(entity="workspace_description", intent=["inform"])
                }

    @staticmethod
    def workspace_type_db():
        types = ["General Workspace","Agile Development"]
        # type: () -> List[Text]
        """Database of supported workspace_type"""
        return types
    
    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""

        try:
            int(string)
            return True
        except ValueError:
            return False

    @staticmethod
    def workspace_name_db(tracker: "Tracker"):
        # type: () -> List[Text]
        """Database of supported names"""
        org_id =  tracker.get_slot('org_id')
        ws_names = ws_service.get_workspacesByName(CreateWorkspaceForm.get_token(),org_id)
        print(ws_names)
        return ws_names
    
    def request_next_slot(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: Dict[Text, Any],
    ) -> Optional[List[EventType]]:
        """Request the next slot and utter template if needed,
            else return None"""

        intent = tracker.latest_message.get("intent", {}).get("name")
        if intent == 'deny':
            return self.deactivate()
        else :

            for slot in self.required_slots(tracker):
                if self._should_request_slot(tracker, slot):

                # Condition to validate org_id
                    if slot == "org_id": 

                        #print("token", self.get_token())

                    # fetch the data and store it in the format used by buttons.
                        org_list = ws_service.get_organisations(token=self.get_token())
                        if not org_list:
                            dispatcher.utter_message(text="you don't have any organisation")
                            return [SlotSet(REQUESTED_SLOT, "0")]

                        dispatcher.utter_message(
                            template=f"utter_ask_{slot}", **tracker.slots, buttons=org_list
                        )

                        return [SlotSet(REQUESTED_SLOT, slot)]

                    logger.debug(f"Request next slot '{slot}'")
                    dispatcher.utter_message(
                    template=f"utter_ask_{slot}", **tracker.slots
                    )
                    return [SlotSet(REQUESTED_SLOT, slot)]
    
    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_template('utter_submit', tracker)
        dispatcher.utter_message("do you confirm workspace creation ?")
        return []
    
    def validate(self,
                 dispatcher: CollectingDispatcher,
                 tracker: Tracker,
                 domain: Dict[Text, Any]) -> List[Dict]:
        """Validate extracted requested slot
            else reject the execution of the form action
        """

        # extract other slots that were not requested
        # but set by corresponding entity
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)

        # extract requested slot
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher,
                                                           tracker, domain))
            print("#### slot_to_fill", slot_to_fill)
            print("#### slot_values", slot_values)

            if slot_to_fill == 'org_id' and not slot_values:
                print("###### tracker.latest_message.text",
                      (tracker.latest_message)['text'])
                # validation failed, set slot to user message
                slot_values['org_id'] = (tracker.latest_message)['text']

            elif slot_to_fill == 'workspace_type' and not slot_values:
                print("###### tracker.latest_message.text",
                      (tracker.latest_message)['text'])
                # validation failed, set slot to user message
                slot_values['workspace_type'] = (tracker.latest_message)['text']

            elif slot_to_fill == 'workspace_name' and not slot_values:
                print("###### tracker.latest_message.text",
                      (tracker.latest_message)['text'])
                # validation failed, set slot to user message
                slot_values['workspace_name'] = (tracker.latest_message)['text']

            elif slot_to_fill == 'workspace_description' and not slot_values:
                print("###### tracker.latest_message.text",
                      (tracker.latest_message)['text'])
                # validation failed, set slot to user message
                slot_values['workspace_description'] = (tracker.latest_message)['text']         


            
            if not slot_values:
                # reject form action execution
                # if some slot was requested but nothing was extracted
                # it will allow other policies to predict another action
                raise ActionExecutionRejection(self.name(),
                                               "Failed to validate slot {0} "
                                               "with action {1}"
                                               "".format(slot_to_fill,
                                                         self.name()))

        for slot, value in slot_values.items():
            if slot == 'workspace_type':
                if value not in self.workspace_type_db() :                    
                    dispatcher.utter_template('utter_wrong_workspace_type', tracker)
                    slot_values[slot] = None

            if slot == 'workspace_name':
                if value in self.workspace_name_db(tracker):
                    dispatcher.utter_template('utter_wrong_workspace_name', tracker)
                    slot_values[slot] = None
                    # validation failed, set slot to None                                    
        # validation succeed, set the slots values to the extracted values

        return [SlotSet(slot, value) for slot, value in slot_values.items()]


        
class ActionCreateWorkspace(Action):
    def name(self):
        """Unique identifier of the form"""
        return 'action_create_workspace'

    def run(self, dispatcher, tracker, domain):
        
        org_id = tracker.get_slot('org_id')
        print("org_id slot : ",org_id)
        
        workspace_type = tracker.get_slot('workspace_type')
        print("workspace_type slot : ",workspace_type)

        workspace_name = tracker.get_slot('workspace_name')
        print("workspace_name slot : ",workspace_name)
        
        workspace_description = tracker.get_slot('workspace_description')
        print("workspace_description slot : ",workspace_description)

        
        
        # create the workspace with graphql
        workspace = ws_service.create_workspace(CreateWorkspaceForm.get_token(),workspace_name,workspace_type,workspace_description,org_id)
        
        if workspace is not None:
            dispatcher.utter_message("workspace successfully created with name: {name} 🚀".format(name=workspace_name))
            tracker.slots['ws_id'] = workspace.get('id')
            print(tracker.slots['ws_id'])
            SlotSet("ws_id", tracker.slots['ws_id'])
            print("*****************collect values of required slots filled before activation")
        # collect values of required slots filled before activation
        

        else :
            print("erorr in graphql *****************")   
        return [SlotSet("ws_id", tracker.slots['ws_id'])]  