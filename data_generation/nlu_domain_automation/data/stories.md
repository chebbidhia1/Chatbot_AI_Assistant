
## say hello
* greet
  - utter_greet

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## interactive_story_1
* greet
    - utter_greet
* name{"name": "omar"}
    - slot{"name": "omar"}
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "548"}
    - slot{"org_id": "548"}
    - form: create_task_form
    - slot{"org_id": "548"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "924"}
    - slot{"ws_id": "924"}
    - form: create_task_form
    - slot{"ws_id": "924"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "687"}
    - slot{"stream_id": "687"}
    - form: create_task_form
    - slot{"stream_id": "687"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "ws chatbot backbones creation"}
    - slot{"task_name": "ws chatbot backbones creation"}
    - form: create_task_form
    - slot{"task_name": "ws chatbot backbones creation"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "30"}
    - slot{"task_priority": "30"}
    - form: create_task_form
    - slot{"task_priority": "30"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - action_create_task
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_2
* greet
    - utter_greet
* name{"name": "nada"}
    - slot{"name": "nada"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "548"}
    - slot{"org_id": "548"}
    - form: create_task_form
    - slot{"org_id": "548"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "1287"}
    - slot{"ws_id": "1287"}
    - form: create_task_form
    - slot{"ws_id": "1287"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "1280"}
    - slot{"stream_id": "1280"}
    - form: create_task_form
    - slot{"stream_id": "1280"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "action create task with chatbot"}
    - slot{"task_name": "action create task with chatbot"}
    - form: create_task_form
    - slot{"task_name": "action create task with chatbot"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "20"}
    - slot{"task_priority": "20"}
    - form: create_task_form
    - slot{"task_priority": "20"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - action_create_task
* goodbye
    - utter_goodbye
    - action_restart

## create task happy path
* greet
    - utter_greet
* name{"name": "jasser"}
    - slot{"name": "jasser"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "548"}
    - slot{"org_id": "548"}
    - form: create_task_form
    - slot{"org_id": "548"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "1287"}
    - slot{"ws_id": "1287"}
    - form: create_task_form
    - slot{"ws_id": "1287"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "1281"}
    - slot{"stream_id": "1281"}
    - form: create_task_form
    - slot{"stream_id": "1281"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "bot testing"}
    - slot{"task_name": "bot testing"}
    - form: create_task_form
    - slot{"task_name": "bot testing"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "30"}
    - slot{"task_priority": "30"}
    - form: create_task_form
    - slot{"task_priority": "30"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - action_create_task
* goodbye
    - utter_goodbye
    - action_restart    


    - utter_goodbye
    - action_restart    

## create task happy path generated story 21 
 * greet
    - utter_greet
* name{"name": "Lila ahahha ahahahhah hahahah aaaaaaaaaaaaaaaaaa"}
    - slot{"name": "Lila ahahha ahahahhah hahahah aaaaaaaaaaaaaaaaaa"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "4820"}
    - slot{"org_id": "4820"}
    - form: create_task_form
    - slot{"org_id": "4820"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "785"}
    - slot{"ws_id": "785"}
    - form: create_task_form
    - slot{"ws_id": "785"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "2639"}
    - slot{"stream_id": "2639"}
    - form: create_task_form
    - slot{"stream_id": "2639"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "explore new features of this program"}
    - slot{"task_name": "explore new features of this program"}
    - form: create_task_form
    - slot{"task_name": "explore new features of this program"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "20"}
    - slot{"task_priority": "20"}
    - form: create_task_form
    - slot{"task_priority": "20"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - action_create_task
* goodbye
    - utter_goodbye
    - action_restart    


    - utter_goodbye
    - action_restart    

## create task happy path generated story 20 
 * greet
    - utter_greet
* name{"name": "Mary Elizabeth"}
    - slot{"name": "Mary Elizabeth"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "6277"}
    - slot{"org_id": "6277"}
    - form: create_task_form
    - slot{"org_id": "6277"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "748"}
    - slot{"ws_id": "748"}
    - form: create_task_form
    - slot{"ws_id": "748"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "5498"}
    - slot{"stream_id": "5498"}
    - form: create_task_form
    - slot{"stream_id": "5498"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "first task"}
    - slot{"task_name": "first task"}
    - form: create_task_form
    - slot{"task_name": "first task"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "0"}
    - slot{"task_priority": "0"}
    - form: create_task_form
    - slot{"task_priority": "0"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - action_create_task
* goodbye
    - utter_goodbye
    - action_restart    


    - utter_goodbye
    - action_restart    

## create task happy path generated story 19 
 * greet
    - utter_greet
* name{"name": "Lila ahahha ahahahhah hahahah aaaaaaaaaaaaaaaaaa"}
    - slot{"name": "Lila ahahha ahahahhah hahahah aaaaaaaaaaaaaaaaaa"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "7239"}
    - slot{"org_id": "7239"}
    - form: create_task_form
    - slot{"org_id": "7239"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "205"}
    - slot{"ws_id": "205"}
    - form: create_task_form
    - slot{"ws_id": "205"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "8779"}
    - slot{"stream_id": "8779"}
    - form: create_task_form
    - slot{"stream_id": "8779"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "build chatbot"}
    - slot{"task_name": "build chatbot"}
    - form: create_task_form
    - slot{"task_name": "build chatbot"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "10"}
    - slot{"task_priority": "10"}
    - form: create_task_form
    - slot{"task_priority": "10"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - action_create_task
* goodbye
    - utter_goodbye
    - action_restart    


    - utter_goodbye
    - action_restart    

## create task happy path generated story 18 
 * greet
    - utter_greet
* name{"name": "Mark-Philip"}
    - slot{"name": "Mark-Philip"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "4820"}
    - slot{"org_id": "4820"}
    - form: create_task_form
    - slot{"org_id": "4820"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "748"}
    - slot{"ws_id": "748"}
    - form: create_task_form
    - slot{"ws_id": "748"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "6543"}
    - slot{"stream_id": "6543"}
    - form: create_task_form
    - slot{"stream_id": "6543"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "master forms on rasa"}
    - slot{"task_name": "master forms on rasa"}
    - form: create_task_form
    - slot{"task_name": "master forms on rasa"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "30"}
    - slot{"task_priority": "30"}
    - form: create_task_form
    - slot{"task_priority": "30"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - action_create_task
* goodbye
    - utter_goodbye
    - action_restart    


    - utter_goodbye
    - action_restart    

## create task happy path generated story 17 
 * greet
    - utter_greet
* name{"name": "Mary Elizabeth"}
    - slot{"name": "Mary Elizabeth"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "8127"}
    - slot{"org_id": "8127"}
    - form: create_task_form
    - slot{"org_id": "8127"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "785"}
    - slot{"ws_id": "785"}
    - form: create_task_form
    - slot{"ws_id": "785"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "8779"}
    - slot{"stream_id": "8779"}
    - form: create_task_form
    - slot{"stream_id": "8779"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "build chatbot"}
    - slot{"task_name": "build chatbot"}
    - form: create_task_form
    - slot{"task_name": "build chatbot"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "10"}
    - slot{"task_priority": "10"}
    - form: create_task_form
    - slot{"task_priority": "10"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - action_create_task
* goodbye
    - utter_goodbye
    - action_restart    


    - utter_goodbye
    - action_restart    

## create task happy path generated story 16 
 * greet
    - utter_greet
* name{"name": "Jack James"}
    - slot{"name": "Jack James"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "8127"}
    - slot{"org_id": "8127"}
    - form: create_task_form
    - slot{"org_id": "8127"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "205"}
    - slot{"ws_id": "205"}
    - form: create_task_form
    - slot{"ws_id": "205"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "2639"}
    - slot{"stream_id": "2639"}
    - form: create_task_form
    - slot{"stream_id": "2639"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "develop new techniques to improve the program"}
    - slot{"task_name": "develop new techniques to improve the program"}
    - form: create_task_form
    - slot{"task_name": "develop new techniques to improve the program"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "20"}
    - slot{"task_priority": "20"}
    - form: create_task_form
    - slot{"task_priority": "20"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - action_create_task
* goodbye
    - utter_goodbye
    - action_restart    


    - utter_goodbye
    - action_restart    

## create task happy path generated story 15 
 * greet
    - utter_greet
* name{"name": "Lucy Mae"}
    - slot{"name": "Lucy Mae"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "3128"}
    - slot{"org_id": "3128"}
    - form: create_task_form
    - slot{"org_id": "3128"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "965"}
    - slot{"ws_id": "965"}
    - form: create_task_form
    - slot{"ws_id": "965"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "2996"}
    - slot{"stream_id": "2996"}
    - form: create_task_form
    - slot{"stream_id": "2996"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "Establish the requirements stream here"}
    - slot{"task_name": "Establish the requirements stream here"}
    - form: create_task_form
    - slot{"task_name": "Establish the requirements stream here"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "20"}
    - slot{"task_priority": "20"}
    - form: create_task_form
    - slot{"task_priority": "20"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - action_create_task
* goodbye
    - utter_goodbye
    - action_restart    


    - utter_goodbye
    - action_restart    

## create task happy path generated story 14 
 * greet
    - utter_greet
* name{"name": "Jack James"}
    - slot{"name": "Jack James"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "6277"}
    - slot{"org_id": "6277"}
    - form: create_task_form
    - slot{"org_id": "6277"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "205"}
    - slot{"ws_id": "205"}
    - form: create_task_form
    - slot{"ws_id": "205"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "5889"}
    - slot{"stream_id": "5889"}
    - form: create_task_form
    - slot{"stream_id": "5889"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "develop new techniques to improve the program"}
    - slot{"task_name": "develop new techniques to improve the program"}
    - form: create_task_form
    - slot{"task_name": "develop new techniques to improve the program"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "0"}
    - slot{"task_priority": "0"}
    - form: create_task_form
    - slot{"task_priority": "0"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - action_create_task
* goodbye
    - utter_goodbye
    - action_restart    


    - utter_goodbye
    - action_restart    

## create task happy path generated story 13 
 * greet
    - utter_greet
* name{"name": "leila daghfous"}
    - slot{"name": "leila daghfous"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "4820"}
    - slot{"org_id": "4820"}
    - form: create_task_form
    - slot{"org_id": "4820"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "748"}
    - slot{"ws_id": "748"}
    - form: create_task_form
    - slot{"ws_id": "748"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "5498"}
    - slot{"stream_id": "5498"}
    - form: create_task_form
    - slot{"stream_id": "5498"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "master forms on rasa"}
    - slot{"task_name": "master forms on rasa"}
    - form: create_task_form
    - slot{"task_name": "master forms on rasa"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "10"}
    - slot{"task_priority": "10"}
    - form: create_task_form
    - slot{"task_priority": "10"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - action_create_task
* goodbye
    - utter_goodbye
    - action_restart    


    - utter_goodbye
    - action_restart    

## create task happy path generated story 12 
 * greet
    - utter_greet
* name{"name": "leila daghfous"}
    - slot{"name": "leila daghfous"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "7239"}
    - slot{"org_id": "7239"}
    - form: create_task_form
    - slot{"org_id": "7239"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "414"}
    - slot{"ws_id": "414"}
    - form: create_task_form
    - slot{"ws_id": "414"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "2812"}
    - slot{"stream_id": "2812"}
    - form: create_task_form
    - slot{"stream_id": "2812"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "build chatbot"}
    - slot{"task_name": "build chatbot"}
    - form: create_task_form
    - slot{"task_name": "build chatbot"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "0"}
    - slot{"task_priority": "0"}
    - form: create_task_form
    - slot{"task_priority": "0"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - action_create_task
* goodbye
    - utter_goodbye
    - action_restart    


    - utter_goodbye
    - action_restart    

## create task happy path generated story 11 
 * greet
    - utter_greet
* name{"name": "Lila ahahha ahahahhah hahahah aaaaaaaaaaaaaaaaaa"}
    - slot{"name": "Lila ahahha ahahahhah hahahah aaaaaaaaaaaaaaaaaa"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "3128"}
    - slot{"org_id": "3128"}
    - form: create_task_form
    - slot{"org_id": "3128"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "461"}
    - slot{"ws_id": "461"}
    - form: create_task_form
    - slot{"ws_id": "461"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "6543"}
    - slot{"stream_id": "6543"}
    - form: create_task_form
    - slot{"stream_id": "6543"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "first task"}
    - slot{"task_name": "first task"}
    - form: create_task_form
    - slot{"task_name": "first task"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "10"}
    - slot{"task_priority": "10"}
    - form: create_task_form
    - slot{"task_priority": "10"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - action_create_task
* goodbye
    - utter_goodbye
    - action_restart    


    - utter_goodbye
    - action_restart    

## create task happy path generated story 10 
 * greet
    - utter_greet
* name{"name": "Mary Kate"}
    - slot{"name": "Mary Kate"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "6277"}
    - slot{"org_id": "6277"}
    - form: create_task_form
    - slot{"org_id": "6277"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "205"}
    - slot{"ws_id": "205"}
    - form: create_task_form
    - slot{"ws_id": "205"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "5498"}
    - slot{"stream_id": "5498"}
    - form: create_task_form
    - slot{"stream_id": "5498"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "master forms on rasa"}
    - slot{"task_name": "master forms on rasa"}
    - form: create_task_form
    - slot{"task_name": "master forms on rasa"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "10"}
    - slot{"task_priority": "10"}
    - form: create_task_form
    - slot{"task_priority": "10"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - action_create_task
* goodbye
    - utter_goodbye
    - action_restart    


    - utter_goodbye
    - action_restart    

## create task happy path generated story 9 
 * greet
    - utter_greet
* name{"name": "Mary Elizabeth"}
    - slot{"name": "Mary Elizabeth"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "6277"}
    - slot{"org_id": "6277"}
    - form: create_task_form
    - slot{"org_id": "6277"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "965"}
    - slot{"ws_id": "965"}
    - form: create_task_form
    - slot{"ws_id": "965"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "2812"}
    - slot{"stream_id": "2812"}
    - form: create_task_form
    - slot{"stream_id": "2812"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "build chatbot"}
    - slot{"task_name": "build chatbot"}
    - form: create_task_form
    - slot{"task_name": "build chatbot"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "10"}
    - slot{"task_priority": "10"}
    - form: create_task_form
    - slot{"task_priority": "10"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - action_create_task
* goodbye
    - utter_goodbye
    - action_restart    


    - utter_goodbye
    - action_restart    

## create task happy path generated story 8 
 * greet
    - utter_greet
* name{"name": "Lila ahahha ahahahhah hahahah aaaaaaaaaaaaaaaaaa"}
    - slot{"name": "Lila ahahha ahahahhah hahahah aaaaaaaaaaaaaaaaaa"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "6316"}
    - slot{"org_id": "6316"}
    - form: create_task_form
    - slot{"org_id": "6316"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "414"}
    - slot{"ws_id": "414"}
    - form: create_task_form
    - slot{"ws_id": "414"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "5889"}
    - slot{"stream_id": "5889"}
    - form: create_task_form
    - slot{"stream_id": "5889"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "enrich knowledge about graphql"}
    - slot{"task_name": "enrich knowledge about graphql"}
    - form: create_task_form
    - slot{"task_name": "enrich knowledge about graphql"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "30"}
    - slot{"task_priority": "30"}
    - form: create_task_form
    - slot{"task_priority": "30"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - action_create_task
* goodbye
    - utter_goodbye
    - action_restart    


    - utter_goodbye
    - action_restart    

## create task happy path generated story 7 
 * greet
    - utter_greet
* name{"name": "Lila ahahha ahahahhah hahahah aaaaaaaaaaaaaaaaaa"}
    - slot{"name": "Lila ahahha ahahahhah hahahah aaaaaaaaaaaaaaaaaa"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "6277"}
    - slot{"org_id": "6277"}
    - form: create_task_form
    - slot{"org_id": "6277"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "965"}
    - slot{"ws_id": "965"}
    - form: create_task_form
    - slot{"ws_id": "965"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "2996"}
    - slot{"stream_id": "2996"}
    - form: create_task_form
    - slot{"stream_id": "2996"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "enrich knowledge about graphql"}
    - slot{"task_name": "enrich knowledge about graphql"}
    - form: create_task_form
    - slot{"task_name": "enrich knowledge about graphql"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "0"}
    - slot{"task_priority": "0"}
    - form: create_task_form
    - slot{"task_priority": "0"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - action_create_task
* goodbye
    - utter_goodbye
    - action_restart    


    - utter_goodbye
    - action_restart    

## create task happy path generated story 6 
 * greet
    - utter_greet
* name{"name": "Jack James"}
    - slot{"name": "Jack James"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "3128"}
    - slot{"org_id": "3128"}
    - form: create_task_form
    - slot{"org_id": "3128"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "461"}
    - slot{"ws_id": "461"}
    - form: create_task_form
    - slot{"ws_id": "461"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "6543"}
    - slot{"stream_id": "6543"}
    - form: create_task_form
    - slot{"stream_id": "6543"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "Establish the requirements stream here"}
    - slot{"task_name": "Establish the requirements stream here"}
    - form: create_task_form
    - slot{"task_name": "Establish the requirements stream here"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "0"}
    - slot{"task_priority": "0"}
    - form: create_task_form
    - slot{"task_priority": "0"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - action_create_task
* goodbye
    - utter_goodbye
    - action_restart    


    - utter_goodbye
    - action_restart    

## create task happy path generated story 5 
 * greet
    - utter_greet
* name{"name": "Jack James"}
    - slot{"name": "Jack James"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "3128"}
    - slot{"org_id": "3128"}
    - form: create_task_form
    - slot{"org_id": "3128"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "14"}
    - slot{"ws_id": "14"}
    - form: create_task_form
    - slot{"ws_id": "14"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "2639"}
    - slot{"stream_id": "2639"}
    - form: create_task_form
    - slot{"stream_id": "2639"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "build chatbot"}
    - slot{"task_name": "build chatbot"}
    - form: create_task_form
    - slot{"task_name": "build chatbot"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "10"}
    - slot{"task_priority": "10"}
    - form: create_task_form
    - slot{"task_priority": "10"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - action_create_task
* goodbye
    - utter_goodbye
    - action_restart    


    - utter_goodbye
    - action_restart    

## create task happy path generated story 4 
 * greet
    - utter_greet
* name{"name": "Mark-Philip"}
    - slot{"name": "Mark-Philip"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "4820"}
    - slot{"org_id": "4820"}
    - form: create_task_form
    - slot{"org_id": "4820"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "205"}
    - slot{"ws_id": "205"}
    - form: create_task_form
    - slot{"ws_id": "205"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "6543"}
    - slot{"stream_id": "6543"}
    - form: create_task_form
    - slot{"stream_id": "6543"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "enrich knowledge about graphql"}
    - slot{"task_name": "enrich knowledge about graphql"}
    - form: create_task_form
    - slot{"task_name": "enrich knowledge about graphql"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "0"}
    - slot{"task_priority": "0"}
    - form: create_task_form
    - slot{"task_priority": "0"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - action_create_task
* goodbye
    - utter_goodbye
    - action_restart    


    - utter_goodbye
    - action_restart    

## create task happy path generated story 3 
 * greet
    - utter_greet
* name{"name": "Lucy Mae"}
    - slot{"name": "Lucy Mae"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "3128"}
    - slot{"org_id": "3128"}
    - form: create_task_form
    - slot{"org_id": "3128"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "785"}
    - slot{"ws_id": "785"}
    - form: create_task_form
    - slot{"ws_id": "785"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "2996"}
    - slot{"stream_id": "2996"}
    - form: create_task_form
    - slot{"stream_id": "2996"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "explore new features of this program"}
    - slot{"task_name": "explore new features of this program"}
    - form: create_task_form
    - slot{"task_name": "explore new features of this program"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "0"}
    - slot{"task_priority": "0"}
    - form: create_task_form
    - slot{"task_priority": "0"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - action_create_task
* goodbye
    - utter_goodbye
    - action_restart    


    - utter_goodbye
    - action_restart    

## create task happy path generated story 2 
 * greet
    - utter_greet
* name{"name": "Lila ahahha ahahahhah hahahah aaaaaaaaaaaaaaaaaa"}
    - slot{"name": "Lila ahahha ahahahhah hahahah aaaaaaaaaaaaaaaaaa"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "7333"}
    - slot{"org_id": "7333"}
    - form: create_task_form
    - slot{"org_id": "7333"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "14"}
    - slot{"ws_id": "14"}
    - form: create_task_form
    - slot{"ws_id": "14"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "8779"}
    - slot{"stream_id": "8779"}
    - form: create_task_form
    - slot{"stream_id": "8779"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "build chatbot"}
    - slot{"task_name": "build chatbot"}
    - form: create_task_form
    - slot{"task_name": "build chatbot"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "20"}
    - slot{"task_priority": "20"}
    - form: create_task_form
    - slot{"task_priority": "20"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - action_create_task
* goodbye
    - utter_goodbye
    - action_restart    


    - utter_goodbye
    - action_restart    

## create task happy path generated story 1 
 * greet
    - utter_greet
* name{"name": "Lucy Mae"}
    - slot{"name": "Lucy Mae"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "8127"}
    - slot{"org_id": "8127"}
    - form: create_task_form
    - slot{"org_id": "8127"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "748"}
    - slot{"ws_id": "748"}
    - form: create_task_form
    - slot{"ws_id": "748"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "5498"}
    - slot{"stream_id": "5498"}
    - form: create_task_form
    - slot{"stream_id": "5498"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "build chatbot"}
    - slot{"task_name": "build chatbot"}
    - form: create_task_form
    - slot{"task_name": "build chatbot"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "10"}
    - slot{"task_priority": "10"}
    - form: create_task_form
    - slot{"task_priority": "10"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - action_create_task
* goodbye
    - utter_goodbye
    - action_restart    


    - utter_goodbye
    - action_restart    

## create task happy path 1
* greet
    - utter_greet
* name{"name": "jasser"}
    - slot{"name": "jasser"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "548"}
    - slot{"org_id": "548"}
    - form: create_task_form
    - slot{"org_id": "548"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "1287"}
    - slot{"ws_id": "1287"}
    - form: create_task_form
    - slot{"ws_id": "1287"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "1281"}
    - slot{"stream_id": "1281"}
    - form: create_task_form
    - slot{"stream_id": "1281"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "bot testing"}
    - slot{"task_name": "bot testing"}
    - form: create_task_form
    - slot{"task_name": "bot testing"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "30"}
    - slot{"task_priority": "30"}
    - form: create_task_form
    - slot{"task_priority": "30"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - action_create_task
* goodbye
    - utter_goodbye
    - action_restart    

## create task happy path 2
* greet
    - utter_greet
* name{"name": "nada"}
    - slot{"name": "nada"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "548"}
    - slot{"org_id": "548"}
    - form: create_task_form
    - slot{"org_id": "548"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "1287"}
    - slot{"ws_id": "1287"}
    - form: create_task_form
    - slot{"ws_id": "1287"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "1280"}
    - slot{"stream_id": "1280"}
    - form: create_task_form
    - slot{"stream_id": "1280"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "action create task with chatbot"}
    - slot{"task_name": "action create task with chatbot"}
    - form: create_task_form
    - slot{"task_name": "action create task with chatbot"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "20"}
    - slot{"task_priority": "20"}
    - form: create_task_form
    - slot{"task_priority": "20"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - action_create_task
* goodbye
    - utter_goodbye
    - action_restart

## create task happy path 3
* greet
    - utter_greet
* name{"name": "mahdi"}
    - slot{"name": "mahdi"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "348"}
    - slot{"org_id": "348"}
    - form: create_task_form
    - slot{"org_id": "348"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "2087"}
    - slot{"ws_id": "2087"}
    - form: create_task_form
    - slot{"ws_id": "2087"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "1271"}
    - slot{"stream_id": "1271"}
    - form: create_task_form
    - slot{"stream_id": "1271"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "bot creation"}
    - slot{"task_name": "bot creation"}
    - form: create_task_form
    - slot{"task_name": "bot creation"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "20"}
    - slot{"task_priority": "20"}
    - form: create_task_form
    - slot{"task_priority": "20"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - action_create_task
* goodbye
    - utter_goodbye
    - action_restart

## create task happy path 4
* greet
    - utter_greet
* name{"name": "mahdi"}
    - slot{"name": "mahdi"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "348"}
    - slot{"org_id": "348"}
    - form: create_task_form
    - slot{"org_id": "348"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "2087"}
    - slot{"ws_id": "2087"}
    - form: create_task_form
    - slot{"ws_id": "2087"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "1271"}
    - slot{"stream_id": "1271"}
    - form: create_task_form
    - slot{"stream_id": "1271"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "bot creation"}
    - slot{"task_name": "bot creation"}
    - form: create_task_form
    - slot{"task_name": "bot creation"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "20"}
    - slot{"task_priority": "20"}
    - form: create_task_form
    - slot{"task_priority": "20"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - action_create_task
* goodbye
    - utter_goodbye    
    - action_restart

## create task happy path 5
* greet
    - utter_greet
* name{"name": "mahdi"}
    - slot{"name": "mahdi"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "148"}
    - slot{"org_id": "148"}
    - form: create_task_form
    - slot{"org_id": "148"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "1587"}
    - slot{"ws_id": "1587"}
    - form: create_task_form
    - slot{"ws_id": "1587"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "2271"}
    - slot{"stream_id": "2271"}
    - form: create_task_form
    - slot{"stream_id": "2271"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "create nlu data"}
    - slot{"task_name": "create nlu data"}
    - form: create_task_form
    - slot{"task_name": "create nlu data"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "10"}
    - slot{"task_priority": "10"}
    - form: create_task_form
    - slot{"task_priority": "10"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - action_create_task
* goodbye
    - utter_goodbye    
    - action_restart  

## "create task" stop but continue (deny) path
* greet
    - utter_greet
* name{"name": "mahdi"}
    - slot{"name": "mahdi"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "148"}
    - slot{"org_id": "148"}
    - form: create_task_form
    - slot{"org_id": "148"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "1587"}
    - slot{"ws_id": "1587"}
    - form: create_task_form
    - slot{"ws_id": "1587"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "2271"}
    - slot{"stream_id": "2271"}
    - form: create_task_form
    - slot{"stream_id": "2271"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "create nlu data"}
    - slot{"task_name": "create nlu data"}
    - form: create_task_form
    - slot{"task_name": "create nlu data"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "10"}
    - slot{"task_priority": "10"}
    - form: create_task_form
    - slot{"task_priority": "10"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* affirm
    - action_create_task
* goodbye
    - utter_goodbye    
    - action_restart  

## "create task" stop but continue (deny) path generated story 14 
 * greet
    - utter_greet
* name{"name": "leila daghfous"}
    - slot{"name": "leila daghfous"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "7239"}
    - slot{"org_id": "7239"}
    - form: create_task_form
    - slot{"org_id": "7239"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "414"}
    - slot{"ws_id": "414"}
    - form: create_task_form
    - slot{"ws_id": "414"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "6543"}
    - slot{"stream_id": "6543"}
    - form: create_task_form
    - slot{"stream_id": "6543"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "develop new techniques to improve the program"}
    - slot{"task_name": "develop new techniques to improve the program"}
    - form: create_task_form
    - slot{"task_name": "develop new techniques to improve the program"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "0"}
    - slot{"task_priority": "0"}
    - form: create_task_form
    - slot{"task_priority": "0"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* affirm
    - action_create_task
* goodbye
    - utter_goodbye    
    - action_restart  

## "create task" stop but continue (deny) path generated story 13 
 * greet
    - utter_greet
* name{"name": "Mark-Philip"}
    - slot{"name": "Mark-Philip"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "7333"}
    - slot{"org_id": "7333"}
    - form: create_task_form
    - slot{"org_id": "7333"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "205"}
    - slot{"ws_id": "205"}
    - form: create_task_form
    - slot{"ws_id": "205"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "2812"}
    - slot{"stream_id": "2812"}
    - form: create_task_form
    - slot{"stream_id": "2812"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "first task"}
    - slot{"task_name": "first task"}
    - form: create_task_form
    - slot{"task_name": "first task"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "20"}
    - slot{"task_priority": "20"}
    - form: create_task_form
    - slot{"task_priority": "20"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* affirm
    - action_create_task
* goodbye
    - utter_goodbye    
    - action_restart  

## "create task" stop but continue (deny) path generated story 12 
 * greet
    - utter_greet
* name{"name": "Jack James"}
    - slot{"name": "Jack James"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "3128"}
    - slot{"org_id": "3128"}
    - form: create_task_form
    - slot{"org_id": "3128"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "785"}
    - slot{"ws_id": "785"}
    - form: create_task_form
    - slot{"ws_id": "785"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "5498"}
    - slot{"stream_id": "5498"}
    - form: create_task_form
    - slot{"stream_id": "5498"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "build chatbot"}
    - slot{"task_name": "build chatbot"}
    - form: create_task_form
    - slot{"task_name": "build chatbot"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "20"}
    - slot{"task_priority": "20"}
    - form: create_task_form
    - slot{"task_priority": "20"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* affirm
    - action_create_task
* goodbye
    - utter_goodbye    
    - action_restart  

## "create task" stop but continue (deny) path generated story 11 
 * greet
    - utter_greet
* name{"name": "leila daghfous"}
    - slot{"name": "leila daghfous"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "7239"}
    - slot{"org_id": "7239"}
    - form: create_task_form
    - slot{"org_id": "7239"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "414"}
    - slot{"ws_id": "414"}
    - form: create_task_form
    - slot{"ws_id": "414"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "6543"}
    - slot{"stream_id": "6543"}
    - form: create_task_form
    - slot{"stream_id": "6543"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "Establish the requirements stream here"}
    - slot{"task_name": "Establish the requirements stream here"}
    - form: create_task_form
    - slot{"task_name": "Establish the requirements stream here"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "0"}
    - slot{"task_priority": "0"}
    - form: create_task_form
    - slot{"task_priority": "0"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* affirm
    - action_create_task
* goodbye
    - utter_goodbye    
    - action_restart  

## "create task" stop but continue (deny) path generated story 10 
 * greet
    - utter_greet
* name{"name": "leila daghfous"}
    - slot{"name": "leila daghfous"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "7333"}
    - slot{"org_id": "7333"}
    - form: create_task_form
    - slot{"org_id": "7333"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "414"}
    - slot{"ws_id": "414"}
    - form: create_task_form
    - slot{"ws_id": "414"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "8779"}
    - slot{"stream_id": "8779"}
    - form: create_task_form
    - slot{"stream_id": "8779"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "develop new techniques to improve the program"}
    - slot{"task_name": "develop new techniques to improve the program"}
    - form: create_task_form
    - slot{"task_name": "develop new techniques to improve the program"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "10"}
    - slot{"task_priority": "10"}
    - form: create_task_form
    - slot{"task_priority": "10"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* affirm
    - action_create_task
* goodbye
    - utter_goodbye    
    - action_restart  

## "create task" stop but continue (deny) path generated story 9 
 * greet
    - utter_greet
* name{"name": "Lila ahahha ahahahhah hahahah aaaaaaaaaaaaaaaaaa"}
    - slot{"name": "Lila ahahha ahahahhah hahahah aaaaaaaaaaaaaaaaaa"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "4820"}
    - slot{"org_id": "4820"}
    - form: create_task_form
    - slot{"org_id": "4820"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "461"}
    - slot{"ws_id": "461"}
    - form: create_task_form
    - slot{"ws_id": "461"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "6543"}
    - slot{"stream_id": "6543"}
    - form: create_task_form
    - slot{"stream_id": "6543"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "master forms on rasa"}
    - slot{"task_name": "master forms on rasa"}
    - form: create_task_form
    - slot{"task_name": "master forms on rasa"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "0"}
    - slot{"task_priority": "0"}
    - form: create_task_form
    - slot{"task_priority": "0"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* affirm
    - action_create_task
* goodbye
    - utter_goodbye    
    - action_restart  

## "create task" stop but continue (deny) path generated story 8 
 * greet
    - utter_greet
* name{"name": "Mark-Philip"}
    - slot{"name": "Mark-Philip"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "8127"}
    - slot{"org_id": "8127"}
    - form: create_task_form
    - slot{"org_id": "8127"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "965"}
    - slot{"ws_id": "965"}
    - form: create_task_form
    - slot{"ws_id": "965"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "8779"}
    - slot{"stream_id": "8779"}
    - form: create_task_form
    - slot{"stream_id": "8779"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "develop new techniques to improve the program"}
    - slot{"task_name": "develop new techniques to improve the program"}
    - form: create_task_form
    - slot{"task_name": "develop new techniques to improve the program"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "30"}
    - slot{"task_priority": "30"}
    - form: create_task_form
    - slot{"task_priority": "30"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* affirm
    - action_create_task
* goodbye
    - utter_goodbye    
    - action_restart  

## "create task" stop but continue (deny) path generated story 7 
 * greet
    - utter_greet
* name{"name": "Mark-Philip"}
    - slot{"name": "Mark-Philip"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "7333"}
    - slot{"org_id": "7333"}
    - form: create_task_form
    - slot{"org_id": "7333"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "785"}
    - slot{"ws_id": "785"}
    - form: create_task_form
    - slot{"ws_id": "785"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "2812"}
    - slot{"stream_id": "2812"}
    - form: create_task_form
    - slot{"stream_id": "2812"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "first task"}
    - slot{"task_name": "first task"}
    - form: create_task_form
    - slot{"task_name": "first task"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "30"}
    - slot{"task_priority": "30"}
    - form: create_task_form
    - slot{"task_priority": "30"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* affirm
    - action_create_task
* goodbye
    - utter_goodbye    
    - action_restart  

## "create task" stop but continue (deny) path generated story 6 
 * greet
    - utter_greet
* name{"name": "Mary Elizabeth"}
    - slot{"name": "Mary Elizabeth"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "6316"}
    - slot{"org_id": "6316"}
    - form: create_task_form
    - slot{"org_id": "6316"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "748"}
    - slot{"ws_id": "748"}
    - form: create_task_form
    - slot{"ws_id": "748"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "2639"}
    - slot{"stream_id": "2639"}
    - form: create_task_form
    - slot{"stream_id": "2639"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "Establish the requirements stream here"}
    - slot{"task_name": "Establish the requirements stream here"}
    - form: create_task_form
    - slot{"task_name": "Establish the requirements stream here"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "20"}
    - slot{"task_priority": "20"}
    - form: create_task_form
    - slot{"task_priority": "20"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* affirm
    - action_create_task
* goodbye
    - utter_goodbye    
    - action_restart  

## "create task" stop but continue (deny) path generated story 5 
 * greet
    - utter_greet
* name{"name": "Lucy Mae"}
    - slot{"name": "Lucy Mae"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "4820"}
    - slot{"org_id": "4820"}
    - form: create_task_form
    - slot{"org_id": "4820"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "965"}
    - slot{"ws_id": "965"}
    - form: create_task_form
    - slot{"ws_id": "965"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "6543"}
    - slot{"stream_id": "6543"}
    - form: create_task_form
    - slot{"stream_id": "6543"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "master forms on rasa"}
    - slot{"task_name": "master forms on rasa"}
    - form: create_task_form
    - slot{"task_name": "master forms on rasa"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "20"}
    - slot{"task_priority": "20"}
    - form: create_task_form
    - slot{"task_priority": "20"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* affirm
    - action_create_task
* goodbye
    - utter_goodbye    
    - action_restart  

## "create task" stop but continue (deny) path generated story 4 
 * greet
    - utter_greet
* name{"name": "leila daghfous"}
    - slot{"name": "leila daghfous"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "4820"}
    - slot{"org_id": "4820"}
    - form: create_task_form
    - slot{"org_id": "4820"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "785"}
    - slot{"ws_id": "785"}
    - form: create_task_form
    - slot{"ws_id": "785"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "6543"}
    - slot{"stream_id": "6543"}
    - form: create_task_form
    - slot{"stream_id": "6543"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "master forms on rasa"}
    - slot{"task_name": "master forms on rasa"}
    - form: create_task_form
    - slot{"task_name": "master forms on rasa"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "10"}
    - slot{"task_priority": "10"}
    - form: create_task_form
    - slot{"task_priority": "10"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* affirm
    - action_create_task
* goodbye
    - utter_goodbye    
    - action_restart  

## "create task" stop but continue (deny) path generated story 3 
 * greet
    - utter_greet
* name{"name": "leila daghfous"}
    - slot{"name": "leila daghfous"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "3128"}
    - slot{"org_id": "3128"}
    - form: create_task_form
    - slot{"org_id": "3128"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "785"}
    - slot{"ws_id": "785"}
    - form: create_task_form
    - slot{"ws_id": "785"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "5498"}
    - slot{"stream_id": "5498"}
    - form: create_task_form
    - slot{"stream_id": "5498"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "master forms on rasa"}
    - slot{"task_name": "master forms on rasa"}
    - form: create_task_form
    - slot{"task_name": "master forms on rasa"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "20"}
    - slot{"task_priority": "20"}
    - form: create_task_form
    - slot{"task_priority": "20"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* affirm
    - action_create_task
* goodbye
    - utter_goodbye    
    - action_restart  

## "create task" stop but continue (deny) path generated story 2 
 * greet
    - utter_greet
* name{"name": "Lila ahahha ahahahhah hahahah aaaaaaaaaaaaaaaaaa"}
    - slot{"name": "Lila ahahha ahahahhah hahahah aaaaaaaaaaaaaaaaaa"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "7239"}
    - slot{"org_id": "7239"}
    - form: create_task_form
    - slot{"org_id": "7239"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "205"}
    - slot{"ws_id": "205"}
    - form: create_task_form
    - slot{"ws_id": "205"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "8779"}
    - slot{"stream_id": "8779"}
    - form: create_task_form
    - slot{"stream_id": "8779"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "first task"}
    - slot{"task_name": "first task"}
    - form: create_task_form
    - slot{"task_name": "first task"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "20"}
    - slot{"task_priority": "20"}
    - form: create_task_form
    - slot{"task_priority": "20"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* affirm
    - action_create_task
* goodbye
    - utter_goodbye    
    - action_restart  

## "create task" stop but continue (deny) path generated story 1 
 * greet
    - utter_greet
* name{"name": "Mary Elizabeth"}
    - slot{"name": "Mary Elizabeth"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "4820"}
    - slot{"org_id": "4820"}
    - form: create_task_form
    - slot{"org_id": "4820"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "785"}
    - slot{"ws_id": "785"}
    - form: create_task_form
    - slot{"ws_id": "785"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "5889"}
    - slot{"stream_id": "5889"}
    - form: create_task_form
    - slot{"stream_id": "5889"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "enrich knowledge about graphql"}
    - slot{"task_name": "enrich knowledge about graphql"}
    - form: create_task_form
    - slot{"task_name": "enrich knowledge about graphql"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "0"}
    - slot{"task_priority": "0"}
    - form: create_task_form
    - slot{"task_priority": "0"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* affirm
    - action_create_task
* goodbye
    - utter_goodbye    
    - action_restart  

## "create task" stop but continue (deny) path 1
* greet
    - utter_greet
* name{"name": "mahdi"}
    - slot{"name": "mahdi"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "148"}
    - slot{"org_id": "148"}
    - form: create_task_form
    - slot{"org_id": "148"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "1587"}
    - slot{"ws_id": "1587"}
    - form: create_task_form
    - slot{"ws_id": "1587"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "2271"}
    - slot{"stream_id": "2271"}
    - form: create_task_form
    - slot{"stream_id": "2271"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "create nlu data"}
    - slot{"task_name": "create nlu data"}
    - form: create_task_form
    - slot{"task_name": "create nlu data"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "10"}
    - slot{"task_priority": "10"}
    - form: create_task_form
    - slot{"task_priority": "10"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* affirm
    - action_create_task
* goodbye
    - utter_goodbye    
    - action_restart  

## "create task" stop but continue (deny) path 2
* greet
    - utter_greet
* name{"name": "nada"}
    - slot{"name": "nada"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "318"}
    - slot{"org_id": "318"}
    - form: create_task_form
    - slot{"org_id": "318"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "187"}
    - slot{"ws_id": "187"}
    - form: create_task_form
    - slot{"ws_id": "187"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "2531"}
    - slot{"stream_id": "2531"}
    - form: create_task_form
    - slot{"stream_id": "2531"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "create stories data"}
    - slot{"task_name": "create stories data"}
    - form: create_task_form
    - slot{"task_name": "create stories data"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "10"}
    - slot{"task_priority": "10"}
    - form: create_task_form
    - slot{"task_priority": "10"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* affirm
    - action_create_task
* goodbye
    - utter_goodbye    
    - action_restart   

## "create task" stop but continue (deny) path 3
* greet
    - utter_greet
* name{"name": "syrine"}
    - slot{"name": "syrine"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "501"}
    - slot{"org_id": "501"}
    - form: create_task_form
    - slot{"org_id": "501"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "4187"}
    - slot{"ws_id": "4187"}
    - form: create_task_form
    - slot{"ws_id": "4187"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "2532"}
    - slot{"stream_id": "2532"}
    - form: create_task_form
    - slot{"stream_id": "2532"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "create config"}
    - slot{"task_name": "create config"}
    - form: create_task_form
    - slot{"task_name": "create config"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "30"}
    - slot{"task_priority": "30"}
    - form: create_task_form
    - slot{"task_priority": "30"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* affirm
    - action_create_task
* goodbye
    - utter_goodbye    
    - action_restart 

## "create task" stop but continue (deny) path 4
* greet
    - utter_greet
* name{"name": "omar"}
    - slot{"name": "omar"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "201"}
    - slot{"org_id": "201"}
    - form: create_task_form
    - slot{"org_id": "201"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "1787"}
    - slot{"ws_id": "1787"}
    - form: create_task_form
    - slot{"ws_id": "1787"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "2832"}
    - slot{"stream_id": "2832"}
    - form: create_task_form
    - slot{"stream_id": "2832"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "create glue scripts"}
    - slot{"task_name": "create glue scripts"}
    - form: create_task_form
    - slot{"task_name": "create glue scripts"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "20"}
    - slot{"task_priority": "20"}
    - form: create_task_form
    - slot{"task_priority": "20"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* affirm
    - action_create_task
* goodbye
    - utter_goodbye    
    - action_restart 

## "create task" stop but continue (deny) path 5
* greet
    - utter_greet
* name{"name": "ali"}
    - slot{"name": "ali"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "1"}
    - slot{"org_id": "1"}
    - form: create_task_form
    - slot{"org_id": "1"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "7"}
    - slot{"ws_id": "7"}
    - form: create_task_form
    - slot{"ws_id": "7"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "12"}
    - slot{"stream_id": "12"}
    - form: create_task_form
    - slot{"stream_id": "12"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "create lambda functions"}
    - slot{"task_name": "create lambda functions"}
    - form: create_task_form
    - slot{"task_name": "create lambda functions"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "20"}
    - slot{"task_priority": "20"}
    - form: create_task_form
    - slot{"task_priority": "20"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* affirm
    - action_create_task
* goodbye
    - utter_goodbye    
    - action_restart                  

## "create task" stop and really stop (deny) path
* greet
    - utter_greet
* name{"name": "mahdi"}
    - slot{"name": "mahdi"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "148"}
    - slot{"org_id": "148"}
    - form: create_task_form
    - slot{"org_id": "148"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "1587"}
    - slot{"ws_id": "1587"}
    - form: create_task_form
    - slot{"ws_id": "1587"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "2271"}
    - slot{"stream_id": "2271"}
    - form: create_task_form
    - slot{"stream_id": "2271"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "create nlu data"}
    - slot{"task_name": "create nlu data"}
    - form: create_task_form
    - slot{"task_name": "create nlu data"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "10"}
    - slot{"task_priority": "10"}
    - form: create_task_form
    - slot{"task_priority": "10"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* deny
    - utter_sorry
    
* goodbye
    - utter_goodbye    
    - action_restart    

## "create task" stop and really stop (deny) path generated story 12 
 * greet
    - utter_greet
* name{"name": "Mark-Philip"}
    - slot{"name": "Mark-Philip"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "4820"}
    - slot{"org_id": "4820"}
    - form: create_task_form
    - slot{"org_id": "4820"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "785"}
    - slot{"ws_id": "785"}
    - form: create_task_form
    - slot{"ws_id": "785"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "2812"}
    - slot{"stream_id": "2812"}
    - form: create_task_form
    - slot{"stream_id": "2812"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "enrich knowledge about graphql"}
    - slot{"task_name": "enrich knowledge about graphql"}
    - form: create_task_form
    - slot{"task_name": "enrich knowledge about graphql"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "20"}
    - slot{"task_priority": "20"}
    - form: create_task_form
    - slot{"task_priority": "20"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* deny
    - utter_sorry
    
* goodbye
    - utter_goodbye    
    - action_restart    

## "create task" stop and really stop (deny) path generated story 11 
 * greet
    - utter_greet
* name{"name": "Mark-Philip"}
    - slot{"name": "Mark-Philip"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "6277"}
    - slot{"org_id": "6277"}
    - form: create_task_form
    - slot{"org_id": "6277"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "414"}
    - slot{"ws_id": "414"}
    - form: create_task_form
    - slot{"ws_id": "414"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "6543"}
    - slot{"stream_id": "6543"}
    - form: create_task_form
    - slot{"stream_id": "6543"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "explore new features of this program"}
    - slot{"task_name": "explore new features of this program"}
    - form: create_task_form
    - slot{"task_name": "explore new features of this program"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "20"}
    - slot{"task_priority": "20"}
    - form: create_task_form
    - slot{"task_priority": "20"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* deny
    - utter_sorry
    
* goodbye
    - utter_goodbye    
    - action_restart    

## "create task" stop and really stop (deny) path generated story 10 
 * greet
    - utter_greet
* name{"name": "Lila ahahha ahahahhah hahahah aaaaaaaaaaaaaaaaaa"}
    - slot{"name": "Lila ahahha ahahahhah hahahah aaaaaaaaaaaaaaaaaa"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "7333"}
    - slot{"org_id": "7333"}
    - form: create_task_form
    - slot{"org_id": "7333"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "748"}
    - slot{"ws_id": "748"}
    - form: create_task_form
    - slot{"ws_id": "748"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "2996"}
    - slot{"stream_id": "2996"}
    - form: create_task_form
    - slot{"stream_id": "2996"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "first task"}
    - slot{"task_name": "first task"}
    - form: create_task_form
    - slot{"task_name": "first task"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "0"}
    - slot{"task_priority": "0"}
    - form: create_task_form
    - slot{"task_priority": "0"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* deny
    - utter_sorry
    
* goodbye
    - utter_goodbye    
    - action_restart    

## "create task" stop and really stop (deny) path generated story 9 
 * greet
    - utter_greet
* name{"name": "Lucy Mae"}
    - slot{"name": "Lucy Mae"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "6277"}
    - slot{"org_id": "6277"}
    - form: create_task_form
    - slot{"org_id": "6277"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "414"}
    - slot{"ws_id": "414"}
    - form: create_task_form
    - slot{"ws_id": "414"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "5889"}
    - slot{"stream_id": "5889"}
    - form: create_task_form
    - slot{"stream_id": "5889"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "master forms on rasa"}
    - slot{"task_name": "master forms on rasa"}
    - form: create_task_form
    - slot{"task_name": "master forms on rasa"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "0"}
    - slot{"task_priority": "0"}
    - form: create_task_form
    - slot{"task_priority": "0"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* deny
    - utter_sorry
    
* goodbye
    - utter_goodbye    
    - action_restart    

## "create task" stop and really stop (deny) path generated story 8 
 * greet
    - utter_greet
* name{"name": "Jack James"}
    - slot{"name": "Jack James"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "7333"}
    - slot{"org_id": "7333"}
    - form: create_task_form
    - slot{"org_id": "7333"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "205"}
    - slot{"ws_id": "205"}
    - form: create_task_form
    - slot{"ws_id": "205"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "2996"}
    - slot{"stream_id": "2996"}
    - form: create_task_form
    - slot{"stream_id": "2996"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "develop new techniques to improve the program"}
    - slot{"task_name": "develop new techniques to improve the program"}
    - form: create_task_form
    - slot{"task_name": "develop new techniques to improve the program"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "20"}
    - slot{"task_priority": "20"}
    - form: create_task_form
    - slot{"task_priority": "20"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* deny
    - utter_sorry
    
* goodbye
    - utter_goodbye    
    - action_restart    

## "create task" stop and really stop (deny) path generated story 7 
 * greet
    - utter_greet
* name{"name": "Mary Elizabeth"}
    - slot{"name": "Mary Elizabeth"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "7333"}
    - slot{"org_id": "7333"}
    - form: create_task_form
    - slot{"org_id": "7333"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "14"}
    - slot{"ws_id": "14"}
    - form: create_task_form
    - slot{"ws_id": "14"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "2812"}
    - slot{"stream_id": "2812"}
    - form: create_task_form
    - slot{"stream_id": "2812"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "develop new techniques to improve the program"}
    - slot{"task_name": "develop new techniques to improve the program"}
    - form: create_task_form
    - slot{"task_name": "develop new techniques to improve the program"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "0"}
    - slot{"task_priority": "0"}
    - form: create_task_form
    - slot{"task_priority": "0"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* deny
    - utter_sorry
    
* goodbye
    - utter_goodbye    
    - action_restart    

## "create task" stop and really stop (deny) path generated story 6 
 * greet
    - utter_greet
* name{"name": "Lila ahahha ahahahhah hahahah aaaaaaaaaaaaaaaaaa"}
    - slot{"name": "Lila ahahha ahahahhah hahahah aaaaaaaaaaaaaaaaaa"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "6316"}
    - slot{"org_id": "6316"}
    - form: create_task_form
    - slot{"org_id": "6316"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "205"}
    - slot{"ws_id": "205"}
    - form: create_task_form
    - slot{"ws_id": "205"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "8779"}
    - slot{"stream_id": "8779"}
    - form: create_task_form
    - slot{"stream_id": "8779"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "first task"}
    - slot{"task_name": "first task"}
    - form: create_task_form
    - slot{"task_name": "first task"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "0"}
    - slot{"task_priority": "0"}
    - form: create_task_form
    - slot{"task_priority": "0"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* deny
    - utter_sorry
    
* goodbye
    - utter_goodbye    
    - action_restart    

## "create task" stop and really stop (deny) path generated story 5 
 * greet
    - utter_greet
* name{"name": "Lila ahahha ahahahhah hahahah aaaaaaaaaaaaaaaaaa"}
    - slot{"name": "Lila ahahha ahahahhah hahahah aaaaaaaaaaaaaaaaaa"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "4820"}
    - slot{"org_id": "4820"}
    - form: create_task_form
    - slot{"org_id": "4820"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "414"}
    - slot{"ws_id": "414"}
    - form: create_task_form
    - slot{"ws_id": "414"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "2639"}
    - slot{"stream_id": "2639"}
    - form: create_task_form
    - slot{"stream_id": "2639"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "develop new techniques to improve the program"}
    - slot{"task_name": "develop new techniques to improve the program"}
    - form: create_task_form
    - slot{"task_name": "develop new techniques to improve the program"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "30"}
    - slot{"task_priority": "30"}
    - form: create_task_form
    - slot{"task_priority": "30"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* deny
    - utter_sorry
    
* goodbye
    - utter_goodbye    
    - action_restart    

## "create task" stop and really stop (deny) path generated story 4 
 * greet
    - utter_greet
* name{"name": "Mary Elizabeth"}
    - slot{"name": "Mary Elizabeth"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "7333"}
    - slot{"org_id": "7333"}
    - form: create_task_form
    - slot{"org_id": "7333"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "414"}
    - slot{"ws_id": "414"}
    - form: create_task_form
    - slot{"ws_id": "414"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "2812"}
    - slot{"stream_id": "2812"}
    - form: create_task_form
    - slot{"stream_id": "2812"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "first task"}
    - slot{"task_name": "first task"}
    - form: create_task_form
    - slot{"task_name": "first task"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "0"}
    - slot{"task_priority": "0"}
    - form: create_task_form
    - slot{"task_priority": "0"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* deny
    - utter_sorry
    
* goodbye
    - utter_goodbye    
    - action_restart    

## "create task" stop and really stop (deny) path generated story 3 
 * greet
    - utter_greet
* name{"name": "leila daghfous"}
    - slot{"name": "leila daghfous"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "6277"}
    - slot{"org_id": "6277"}
    - form: create_task_form
    - slot{"org_id": "6277"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "748"}
    - slot{"ws_id": "748"}
    - form: create_task_form
    - slot{"ws_id": "748"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "5889"}
    - slot{"stream_id": "5889"}
    - form: create_task_form
    - slot{"stream_id": "5889"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "develop new techniques to improve the program"}
    - slot{"task_name": "develop new techniques to improve the program"}
    - form: create_task_form
    - slot{"task_name": "develop new techniques to improve the program"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "20"}
    - slot{"task_priority": "20"}
    - form: create_task_form
    - slot{"task_priority": "20"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* deny
    - utter_sorry
    
* goodbye
    - utter_goodbye    
    - action_restart    

## "create task" stop and really stop (deny) path generated story 2 
 * greet
    - utter_greet
* name{"name": "leila daghfous"}
    - slot{"name": "leila daghfous"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "4820"}
    - slot{"org_id": "4820"}
    - form: create_task_form
    - slot{"org_id": "4820"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "461"}
    - slot{"ws_id": "461"}
    - form: create_task_form
    - slot{"ws_id": "461"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "5498"}
    - slot{"stream_id": "5498"}
    - form: create_task_form
    - slot{"stream_id": "5498"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "master forms on rasa"}
    - slot{"task_name": "master forms on rasa"}
    - form: create_task_form
    - slot{"task_name": "master forms on rasa"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "10"}
    - slot{"task_priority": "10"}
    - form: create_task_form
    - slot{"task_priority": "10"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* deny
    - utter_sorry
    
* goodbye
    - utter_goodbye    
    - action_restart    

## "create task" stop and really stop (deny) path generated story 1 
 * greet
    - utter_greet
* name{"name": "Lucy Mae"}
    - slot{"name": "Lucy Mae"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "6277"}
    - slot{"org_id": "6277"}
    - form: create_task_form
    - slot{"org_id": "6277"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "748"}
    - slot{"ws_id": "748"}
    - form: create_task_form
    - slot{"ws_id": "748"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "2812"}
    - slot{"stream_id": "2812"}
    - form: create_task_form
    - slot{"stream_id": "2812"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "first task"}
    - slot{"task_name": "first task"}
    - form: create_task_form
    - slot{"task_name": "first task"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "0"}
    - slot{"task_priority": "0"}
    - form: create_task_form
    - slot{"task_priority": "0"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* deny
    - utter_sorry
    
* goodbye
    - utter_goodbye    
    - action_restart    

## "create task" stop and really stop (deny) path 1
* greet
    - utter_greet
* name{"name": "mahdi"}
    - slot{"name": "mahdi"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "148"}
    - slot{"org_id": "148"}
    - form: create_task_form
    - slot{"org_id": "148"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "1587"}
    - slot{"ws_id": "1587"}
    - form: create_task_form
    - slot{"ws_id": "1587"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "2271"}
    - slot{"stream_id": "2271"}
    - form: create_task_form
    - slot{"stream_id": "2271"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "create nlu data"}
    - slot{"task_name": "create nlu data"}
    - form: create_task_form
    - slot{"task_name": "create nlu data"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "10"}
    - slot{"task_priority": "10"}
    - form: create_task_form
    - slot{"task_priority": "10"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* deny
    - utter_sorry
    
* goodbye
    - utter_goodbye    
    - action_restart    

## "create task" stop and really stop (deny) path 2
* greet
    - utter_greet
* name{"name": "nada"}
    - slot{"name": "nada"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "318"}
    - slot{"org_id": "318"}
    - form: create_task_form
    - slot{"org_id": "318"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "187"}
    - slot{"ws_id": "187"}
    - form: create_task_form
    - slot{"ws_id": "187"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "2531"}
    - slot{"stream_id": "2531"}
    - form: create_task_form
    - slot{"stream_id": "2531"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "create stories data"}
    - slot{"task_name": "create stories data"}
    - form: create_task_form
    - slot{"task_name": "create stories data"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "10"}
    - slot{"task_priority": "10"}
    - form: create_task_form
    - slot{"task_priority": "10"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* deny
    - utter_sorry
* goodbye
    - utter_goodbye    
    - action_restart       

## "create task" stop and really stop (deny) path 3
* greet
    - utter_greet
* name{"name": "syrine"}
    - slot{"name": "syrine"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "501"}
    - slot{"org_id": "501"}
    - form: create_task_form
    - slot{"org_id": "501"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "4187"}
    - slot{"ws_id": "4187"}
    - form: create_task_form
    - slot{"ws_id": "4187"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "2532"}
    - slot{"stream_id": "2532"}
    - form: create_task_form
    - slot{"stream_id": "2532"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "create config"}
    - slot{"task_name": "create config"}
    - form: create_task_form
    - slot{"task_name": "create config"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "30"}
    - slot{"task_priority": "30"}
    - form: create_task_form
    - slot{"task_priority": "30"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* deny
    - utter_sorry
    
* goodbye
    - utter_goodbye    
    - action_restart    

## "create task" stop and really stop (deny) path 4
* greet
    - utter_greet
* name{"name": "omar"}
    - slot{"name": "omar"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "201"}
    - slot{"org_id": "201"}
    - form: create_task_form
    - slot{"org_id": "201"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "1787"}
    - slot{"ws_id": "1787"}
    - form: create_task_form
    - slot{"ws_id": "1787"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "2832"}
    - slot{"stream_id": "2832"}
    - form: create_task_form
    - slot{"stream_id": "2832"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "create glue scripts"}
    - slot{"task_name": "create glue scripts"}
    - form: create_task_form
    - slot{"task_name": "create glue scripts"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "20"}
    - slot{"task_priority": "20"}
    - form: create_task_form
    - slot{"task_priority": "20"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* deny
    - utter_sorry
    
* goodbye
    - utter_goodbye    
    - action_restart    

## "create task" stop and really stop (deny) path 5
* greet
    - utter_greet
* name{"name": "ali"}
    - slot{"name": "ali"}
    - utter_ask_howcanhelp
* create_task
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "1"}
    - slot{"org_id": "1"}
    - form: create_task_form
    - slot{"org_id": "1"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "7"}
    - slot{"ws_id": "7"}
    - form: create_task_form
    - slot{"ws_id": "7"}
    - slot{"requested_slot": "stream_id"}
* form: inform{"stream_id": "12"}
    - slot{"stream_id": "12"}
    - form: create_task_form
    - slot{"stream_id": "12"}
    - slot{"requested_slot": "task_name"}
* form: inform{"task_name": "create lambda functions"}
    - slot{"task_name": "create lambda functions"}
    - form: create_task_form
    - slot{"task_name": "create lambda functions"}
    - slot{"requested_slot": "task_priority"}
* form: inform{"task_priority": "20"}
    - slot{"task_priority": "20"}
    - form: create_task_form
    - slot{"task_priority": "20"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_ask_continue    
* deny
    - utter_sorry
    
* goodbye
    - utter_goodbye    
    - action_restart    

