
## say hello
* greet: hello
  - utter_greet

## say goodbye
* goodbye: bye 
  - utter_goodbye

## bot challenge
* bot_challenge: are you a bot?
  - utter_iamabot

## interactive_story_1
* greet: hello
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
* affirm: yes
    - action_create_task
* goodbye: bye
    - utter_goodbye
    - action_restart

## interactive_story_2
* greet: hello
    - utter_greet
* name{"name": "nada"}
    - slot{"name": "nada"}
    - utter_ask_howcanhelp
* create_task: i want to add a new task
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
* affirm: yes
    - action_create_task
* goodbye: bye
    - utter_goodbye
    - action_restart

## create task happy path 1
* greet: hello
    - utter_greet
* name{"name": "jasser"}
    - slot{"name": "jasser"}
    - utter_ask_howcanhelp
* create_task: i want to add a new task
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
* affirm: yes
    - action_create_task
* goodbye: bye
    - utter_goodbye
    - action_restart    

## create task happy path 2
* greet: hello
    - utter_greet
* name{"name": "nada"}
    - slot{"name": "nada"}
    - utter_ask_howcanhelp
* create_task: i want to add a new task
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
* affirm: yes
    - action_create_task
* goodbye: bye
    - utter_goodbye
    - action_restart

## create task happy path 3
* greet: hello
    - utter_greet
* name{"name": "mahdi"}
    - slot{"name": "mahdi"}
    - utter_ask_howcanhelp
* create_task: i want to add a new task
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
* affirm: yess
    - action_create_task
* goodbye: bye
    - utter_goodbye
    - action_restart

## create task happy path 4
* greet: hello
    - utter_greet
* name{"name": "mahdi"}
    - slot{"name": "mahdi"}
    - utter_ask_howcanhelp
* create_task: i want to add a new task
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
* affirm: yes
    - action_create_task
* goodbye: bye
    - utter_goodbye    
    - action_restart

## create task happy path 5
* greet: hello
    - utter_greet
* name{"name": "mahdi"}
    - slot{"name": "mahdi"}
    - utter_ask_howcanhelp
* create_task: i want to add a new task
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
* affirm: yes
    - action_create_task
* goodbye: bye
    - utter_goodbye    
    - action_restart  

## "create task" stop but continue (deny) path 1
* greet: hello
    - utter_greet
* name{"name": "mahdi"}
    - slot{"name": "mahdi"}
    - utter_ask_howcanhelp
* create_task: i want to add a new task
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
* deny: no
    - utter_ask_continue    
* affirm: yes
    - action_create_task
* goodbye: bye
    - utter_goodbye    
    - action_restart  

## "create task" stop but continue (deny) path 2
* greet: hello
    - utter_greet
* name{"name": "nada"}
    - slot{"name": "nada"}
    - utter_ask_howcanhelp
* create_task: i want to add a new task
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
* deny: no
    - utter_ask_continue    
* affirm: yes
    - action_create_task
* goodbye: bye
    - utter_goodbye    
    - action_restart   

## "create task" stop but continue (deny) path 3
* greet: hello
    - utter_greet
* name{"name": "syrine"}
    - slot{"name": "syrine"}
    - utter_ask_howcanhelp
* create_task: i want to add a new task
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
* deny: no
    - utter_ask_continue    
* affirm: yes
    - action_create_task
* goodbye: bye
    - utter_goodbye    
    - action_restart 

## "create task" stop but continue (deny) path 4
* greet: hello
    - utter_greet
* name{"name": "omar"}
    - slot{"name": "omar"}
    - utter_ask_howcanhelp
* create_task: i want to add a new task
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
* deny: no
    - utter_ask_continue    
* affirm: yes
    - action_create_task
* goodbye: bye
    - utter_goodbye    
    - action_restart 

## "create task" stop but continue (deny) path 5
* greet: hello
    - utter_greet
* name{"name": "ali"}
    - slot{"name": "ali"}
    - utter_ask_howcanhelp
* create_task: i want to add a new task
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
* deny: no
    - utter_ask_continue    
* affirm: yes
    - action_create_task
* goodbye: bye
    - utter_goodbye    
    - action_restart                  

## "create task" stop and really stop (deny) path 1
* greet: hello
    - utter_greet
* name{"name": "mahdi"}
    - slot{"name": "mahdi"}
    - utter_ask_howcanhelp
* create_task: i want to add a new task
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
* deny: no
    - utter_ask_continue    
* deny: no
    - utter_sorry
    - action_restart

## "create task" stop and really stop (deny) path 2
* greet: hello
    - utter_greet
* name{"name": "nada"}
    - slot{"name": "nada"}
    - utter_ask_howcanhelp
* create_task: i want to add a new task
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
* deny: no
    - utter_ask_continue    
* deny: no
    - utter_sorry
    - action_restart   

## "create task" stop and really stop (deny) path 3
* greet: hello
    - utter_greet
* name{"name": "syrine"}
    - slot{"name": "syrine"}
    - utter_ask_howcanhelp
* create_task: i want to add new task in Task manager
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
* deny: no
    - utter_ask_continue    
* deny: no
    - utter_sorry
    - action_restart

## "create task" stop and really stop (deny) path 4
* greet: hello
    - utter_greet
* name{"name": "omar"}
    - slot{"name": "omar"}
    - utter_ask_howcanhelp
* create_task: i want to add new task in Task manager
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
* deny: no
    - utter_ask_continue    
* deny: no
    - utter_sorry
    - action_restart

## "create task" stop and really stop (deny) path 5
* greet: hello
    - utter_greet
* name{"name": "ali"}
    - slot{"name": "ali"}
    - utter_ask_howcanhelp
* create_task: i want to add new task in Task manager
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
* deny: no
    - utter_ask_continue    
* deny: no
    - utter_sorry
    - action_restart

## interactive_story_1
* greet: hello
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
* affirm: yes
    - action_create_task
* goodbye: bye
    - utter_goodbye
    - action_restart

## interactive_story_create_stream_happy_path_1
* greet: hello
    - utter_greet
* name{"name": "bilel ben brahim"}
    - slot{"name": "bilel ben brahim"}
    - utter_ask_howcanhelp
* create_stream: i want to add a stream
    - create_stream_form
    - form{"name": "create_stream_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "358"}
    - slot{"org_id": "358"}
    - form: create_stream_form
    - slot{"org_id": "358"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "698"}
    - slot{"ws_id": "698"}
    - form: create_stream_form
    - slot{"ws_id": "698"}
    - slot{"requested_slot": "stream_name"}
* form: inform{"stream_name": "front-end validation"}
    - slot{"stream_name": "front-end validation"}
    - form: create_stream_form
    - slot{"stream_name": "front-end validation"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: yes
    - action_create_stream
* goodbye: bye
    - utter_goodbye
    - action_restart   

## interactive_story_create_stream_happy_path_2
* greet: hello
    - utter_greet
* name{"name": "ahmed"}
    - slot{"name": "ahmed"}
    - utter_ask_howcanhelp
* create_stream: i want to add a stream
    - create_stream_form
    - form{"name": "create_stream_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "606"}
    - slot{"org_id": "606"}
    - form: create_stream_form
    - slot{"org_id": "606"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "222"}
    - slot{"ws_id": "222"}
    - form: create_stream_form
    - slot{"ws_id": "222"}
    - slot{"requested_slot": "stream_name"}
* form: inform{"stream_name": "hello rasa"}
    - slot{"stream_name": "hello rasa"}
    - form: create_stream_form
    - slot{"stream_name": "hello rasa"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: yes
    - action_create_stream
* goodbye: bye
    - utter_goodbye
    - action_restart

## interactive_story_create_stream_happy_path_3
* greet: hello
    - utter_greet
* name{"name": "zied tounsi"}
    - slot{"name": "zied tounsi"}
    - utter_ask_howcanhelp
* create_stream: i want to add a stream
    - create_stream_form
    - form{"name": "create_stream_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "100"}
    - slot{"org_id": "100"}
    - form: create_stream_form
    - slot{"org_id": "100"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "401"}
    - slot{"ws_id": "401"}
    - form: create_stream_form
    - slot{"ws_id": "401"}
    - slot{"requested_slot": "stream_name"}
* form: inform{"stream_name": "integration part"}
    - slot{"stream_name": "integration part"}
    - form: create_stream_form
    - slot{"stream_name": "integration part"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: yes
    - action_create_stream
* goodbye: bye
    - utter_goodbye
    - action_restart

## interactive_story_create_workspace_happy_path_1
* greet: hello
    - utter_greet
* name{"name": "syrine slouli"}
    - slot{"name": "syrine slouli"}
    - utter_ask_howcanhelp
* create_workspace: i want to add the workspace
    - create_workspace_form
    - form{"name": "create_workspace_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "100"}
    - slot{"org_id": "100"}
    - form: create_workspace_form
    - slot{"org_id": "100"}
    - slot{"requested_slot": "workspace_type"}
* form: inform{"workspace_type": "General Workspace"}
    - slot{"workspace_type": "General Workspace"}
    - form: create_workspace_form
    - slot{"workspace_type": "General Workspace"}
    - slot{"requested_slot": "workspace_name"}
* form: inform{"workspace_name": "image processing and analysis"}
    - slot{"workspace_name": "image processing and analysis"}
    - form: create_workspace_form
    - slot{"workspace_name": "image processing and analysis"}
    - slot{"requested_slot": "workspace_description"}
* form: inform{"workspace_description": "creating a new workspace type"}
    - slot{"workspace_description": "creating a new workspace type"}
    - form: create_workspace_form
    - slot{"workspace_description": "creating a new workspace type"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: yes
    - action_create_workspace
* goodbye: goodbye
    - utter_goodbye
    - action_restart

## interactive_story_create_workspace_happy_path_2
* greet: hello
    - utter_greet
* name{"name": "mahdi ben ali"}
    - slot{"name": "mahdi ben ali"}
    - utter_ask_howcanhelp
* create_workspace: i want to add the workspace
    - create_workspace_form
    - form{"name": "create_workspace_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "324"}
    - slot{"org_id": "324"}
    - form: create_workspace_form
    - slot{"org_id": "324"}
    - slot{"requested_slot": "workspace_type"}
* form: inform{"workspace_type": "General Workspace"}
    - slot{"workspace_type": "General Workspace"}
    - form: create_workspace_form
    - slot{"workspace_type": "General Workspace"}
    - slot{"requested_slot": "workspace_name"}
* form: inform{"workspace_name": "rasa chatbot deployment"}
    - slot{"workspace_name": "rasa chatbot deployment"}
    - form: create_workspace_form
    - slot{"workspace_name": "rasa chatbot deployment"}
    - slot{"requested_slot": "workspace_description"}
* form: inform{"workspace_description": "target new platform integration"}
    - slot{"workspace_description": "target new platform integration"}
    - form: create_workspace_form
    - slot{"workspace_description": "target new platform integration"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: yes
    - action_create_workspace
* goodbye: goodbye
    - utter_goodbye
    - action_restart

## interactive_story_create_workspace_happy_path_3
* greet: hello
    - utter_greet
* name{"name": "mahdi ben ali"}
    - slot{"name": "mahdi ben ali"}
    - utter_ask_howcanhelp
* create_workspace: i want to add the workspace
    - create_workspace_form
    - form{"name": "create_workspace_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "548"}
    - slot{"org_id": "548"}
    - form: create_workspace_form
    - slot{"org_id": "548"}
    - slot{"requested_slot": "workspace_type"}
* form: inform{"workspace_type": "Agile Development"}
    - slot{"workspace_type": "Agile Development"}
    - form: create_workspace_form
    - slot{"workspace_type": "Agile Development"}
    - slot{"requested_slot": "workspace_name"}
* form: inform{"workspace_name": "Serenity-test-target"}
    - slot{"workspace_name": "Serenity-test-target"}
    - form: create_workspace_form
    - slot{"workspace_name": "Serenity-test-target"}
    - slot{"requested_slot": "workspace_description"}
* form: inform{"workspace_description": "Test workspace"}
    - slot{"workspace_description": "Test workspace"}
    - form: create_workspace_form
    - slot{"workspace_description": "Test workspace"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: yes
    - action_create_workspace
* goodbye: goodbye
    - utter_goodbye
    - action_restart

## interactive_story_create_task_no_stream_found
* greet: hello
    - utter_greet
* name{"name": "melek"}
    - slot{"name": "melek"}
    - utter_ask_howcanhelp
* create_task: i want to add new task in Task manager
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "107"}
    - slot{"org_id": "107"}
    - form: create_task_form
    - slot{"org_id": "107"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "604"}
    - slot{"ws_id": "604"}
    - form: create_task_form
    - slot{"ws_id": "604"}
* change_path: can i change the path ?
    - utter_change_path    
* create_stream: i want to add a stream
    - create_stream_form
    - form{"name": "create_stream_form"}
    - slot{"requested_slot": "stream_name"}
    - form: inform{"stream_name": "training"}
    - slot{"stream_name": "training"}
    - form: create_stream_form
    - slot{"stream_name": "training"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: yes
    - action_create_stream
* create_task: i want to add new task in Task manager
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"stream_id": "1407"}
    - form: create_task_form
    - slot{"stream_id": "1407"}
    - slot{"requested_slot": "task_name"}    
* form: inform{"task_name": "test for test"}
    - slot{"task_name": "test for test"}
    - form: create_task_form
    - slot{"task_name": "test for test"}
    - slot{"requested_slot": "task_priority"}    
* form: inform{"task_priority": "10"}
    - slot{"task_priority": "10"}
    - form: create_task_form
    - slot{"task_priority": "10"}
* deny: no
    - utter_ask_continue   
* affirm: yeah
    - action_create_task
* goodbye: goodbye
    - form{"name": null}
    - form{"name": null}
    - utter_goodbye    
    - action_restart

## interactive_story_create_task_no_stream_found 2
* greet: hello
    - utter_greet
* name{"name": "bilel"}
    - slot{"name": "bilel"}
    - utter_ask_howcanhelp
* create_task: i want to add new task in Task manager
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "508"}
    - slot{"org_id": "508"}
    - form: create_task_form
    - slot{"org_id": "508"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "1006"}
    - slot{"ws_id": "1006"}
    - form: create_task_form
    - slot{"ws_id": "1006"}    
* change_path: can i change the path ?
    - utter_change_path
* create_stream: i want to add a stream
    - create_stream_form
    - form{"name": "create_stream_form"}
    - slot{"requested_slot": "stream_name"}
    - form: inform{"stream_name": "verfication done"}
    - slot{"stream_name": "verfication done"}
    - form: create_stream_form
    - slot{"stream_name": "verfication done"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: yeah
    - action_create_stream
* create_task: i want to add new task in Task manager
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"stream_id": "1207"}
    - form: create_task_form
    - slot{"stream_id": "1207"}
    - slot{"requested_slot": "task_name"}   
    - slot{"task_name": "last step"}
    - form: create_task_form
    - slot{"task_name": "last step"}
    - slot{"requested_slot": "task_priority"}    
* form: inform{"task_priority": "20"}
    - slot{"task_priority": "20"}
    - form: create_task_form
    - slot{"task_priority": "20"}
* deny: no
    - utter_ask_continue   
* affirm: yeah
    - action_create_task
* goodbye: goodbye
    - utter_goodbye 
    - form{"name": null}   
    - action_restart

# interactive_story_create_task_no_stream_found 3
* greet: hello
    - utter_greet
* name{"name": "ahmed jlassi"}
    - slot{"name": "ahmed jlassi"}
    - utter_ask_howcanhelp
* create_task: i want to add new task in Task manager
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "598"}
    - slot{"org_id": "598"}
    - form: create_task_form
    - slot{"org_id": "598"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "409"}
    - slot{"ws_id": "409"}
    - form: create_task_form
    - slot{"ws_id": "409"}
* change_path: can i change the path ?
    - utter_change_path   
* create_stream: i want to add a stream
    - create_stream_form
    - form{"name": "create_stream_form"}
    - slot{"requested_slot": "stream_name"}
    - form: inform{"stream_name": "second strategy"}
    - slot{"stream_name": "second strategy"}
    - form: create_stream_form
    - slot{"stream_name": "second strategy"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: yeah
    - action_create_stream
* create_task: i want to add new task in Task manager
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"stream_id": "1587"}
    - form: create_task_form
    - slot{"stream_id": "1587"}
    - slot{"requested_slot": "task_name"}    
* form: inform{"task_name": "from scratch"}
    - slot{"task_name": "from scratch"}
    - form: create_task_form
    - slot{"task_name": "from scratch"}
    - slot{"requested_slot": "task_priority"}    
* form: inform{"task_priority": "30"}
    - slot{"task_priority": "30"}
    - form: create_task_form
    - slot{"task_priority": "30"}
* deny: no
    - utter_ask_continue   
* affirm: yeah
    - action_create_task
* goodbye: goodbye
    - form{"name": null}
    - utter_goodbye    
    - action_restart

# interactive_story_create_task_no_stream_found 4
* greet: hello
    - utter_greet
* name{"name": "ahmed jlassi"}
    - slot{"name": "ahmed jlassi"}
    - utter_ask_howcanhelp
* create_task: i want to add new task in Task manager
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "598"}
    - slot{"org_id": "598"}
    - form: create_task_form
    - slot{"org_id": "598"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "409"}
    - slot{"ws_id": "409"}
    - form: create_task_form
    - slot{"ws_id": "409"}   
* create_stream: i want to add a stream
    - create_stream_form
    - form{"name": "create_stream_form"}
    - slot{"requested_slot": "stream_name"}
    - form: inform{"stream_name": "second strategy"}
    - slot{"stream_name": "second strategy"}
    - form: create_stream_form
    - slot{"stream_name": "second strategy"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: yeah
    - action_create_stream
* create_task: i want to add new task in Task manager
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"stream_id": "1587"}
    - form: create_task_form
    - slot{"stream_id": "1587"}
    - slot{"requested_slot": "task_name"}    
* form: inform{"task_name": "from scratch"}
    - slot{"task_name": "from scratch"}
    - form: create_task_form
    - slot{"task_name": "from scratch"}
    - slot{"requested_slot": "task_priority"}    
* form: inform{"task_priority": "30"}
    - slot{"task_priority": "30"}
    - form: create_task_form
    - slot{"task_priority": "30"}
* deny: no thanks
    - utter_ask_continue   
* affirm: yeah
    - action_create_task
* goodbye: goodbye
    - form{"name": null}
    - utter_goodbye    
    - action_restart

# interactive_story_create_task_no_stream_found 5
* greet: hello
    - utter_greet
* name{"name": "ahmed jlassi"}
    - slot{"name": "ahmed jlassi"}
    - utter_ask_howcanhelp
* create_task: adding my task in Task manager
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "598"}
    - slot{"org_id": "598"}
    - form: create_task_form
    - slot{"org_id": "598"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "409"}
    - slot{"ws_id": "409"}
    - form: create_task_form
    - slot{"ws_id": "409"}   
* create_stream: i want to add a stream
    - create_stream_form
    - form{"name": "create_stream_form"}
    - slot{"requested_slot": "stream_name"}
    - form: inform{"stream_name": "second strategy"}
    - slot{"stream_name": "second strategy"}
    - form: create_stream_form
    - slot{"stream_name": "second strategy"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: yeah
    - action_create_stream
* create_task: adding my task in Task manager
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"stream_id": "1587"}
    - form: create_task_form
    - slot{"stream_id": "1587"}
    - slot{"requested_slot": "task_name"}    
* form: inform{"task_name": "from scratch"}
    - slot{"task_name": "from scratch"}
    - form: create_task_form
    - slot{"task_name": "from scratch"}
    - slot{"requested_slot": "task_priority"}    
* form: inform{"task_priority": "30"}
    - slot{"task_priority": "30"}
    - form: create_task_form
    - slot{"task_priority": "30"}
* deny: no thanks
    - utter_ask_continue   
* affirm: yeah
    - action_create_task
* goodbye: goodbye
    - form{"name": null}
    - utter_goodbye    
    - action_restart

# interactive_story_create_task_no_stream_found 6
* greet: hello
    - utter_greet
* name{"name": "ahmed jlassi"}
    - slot{"name": "ahmed jlassi"}
    - utter_ask_howcanhelp
* create_task: adding my task in Task manager
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "598"}
    - slot{"org_id": "598"}
    - form: create_task_form
    - slot{"org_id": "598"}
    - slot{"requested_slot": "ws_id"}
* form: inform{"ws_id": "409"}
    - slot{"ws_id": "409"}
    - form: create_task_form
    - slot{"ws_id": "409"}   
* create_stream: i want to add a stream
    - create_stream_form
    - form{"name": "create_stream_form"}
    - slot{"requested_slot": "stream_name"}
    - form: inform{"stream_name": "second strategy"}
    - slot{"stream_name": "second strategy"}
    - form: create_stream_form
    - slot{"stream_name": "second strategy"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: yeah
    - action_create_stream
* create_task: adding my task in Task manager
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"stream_id": "1587"}
    - form: create_task_form
    - slot{"stream_id": "1587"}
    - slot{"requested_slot": "task_name"}    
* form: inform{"task_name": "from scratch"}
    - slot{"task_name": "from scratch"}
    - form: create_task_form
    - slot{"task_name": "from scratch"}
    - slot{"requested_slot": "task_priority"}    
* form: inform{"task_priority": "30"}
    - slot{"task_priority": "30"}
    - form: create_task_form
    - slot{"task_priority": "30"}
* deny: no thanks
    - utter_ask_continue   
* affirm: yeah
    - action_create_task
* goodbye: goodbye
    - form{"name": null}
    - utter_goodbye    
    - action_restart

# interactive_story_create_stream_no_workspace_found 
* greet: hello
    - utter_greet
* name{"name": "ahmed jlassi"}
    - slot{"name": "ahmed jlassi"}
    - utter_ask_howcanhelp
* create_stream: i want to add a stream
    - create_stream_form
    - form{"name": "create_stream_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "358"}
    - slot{"org_id": "358"}
    - form: create_stream_form
    - slot{"org_id": "358"}
* create_workspace: i want to add the workspace
    - create_workspace_form
    - form{"name": "create_workspace_form"}
    - slot{"requested_slot": "workspace_type"}
    - form: inform{"workspace_type": "General Workspace"}
    - slot{"workspace_type": "General Workspace"}
    - form: create_workspace_form
    - slot{"workspace_type": "General Workspace"}
    - slot{"requested_slot": "workspace_name"}
    - form: inform{"workspace_name": "image processing and analysis"}
    - slot{"workspace_name": "image processing and analysis"}
    - form: create_workspace_form
    - slot{"workspace_name": "image processing and analysis"}
    - slot{"requested_slot": "workspace_description"}
    - form: inform{"workspace_description": "creating a new workspace type"}
    - slot{"workspace_description": "creating a new workspace type"}
    - form: create_workspace_form
    - slot{"workspace_description": "creating a new workspace type"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: yeah
    - action_create_workspace
* create_stream: i want to add a stream
    - create_stream_form
    - form{"name": "create_stream_form"}
    - slot{"ws_id": "358"}
    - form: create_stream_form
    - slot{"ws_id": "358"}
    - slot{"requested_slot": "stream_name"}
    - form: inform{"stream_name": "front-end validation"}
    - slot{"stream_name": "front-end validation"}
    - form: create_stream_form
    - slot{"stream_name": "front-end validation"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* deny: no thanks
    - utter_ask_continue
* affirm: yeah
    - action_create_stream
* goodbye: goodbye
    
    - utter_goodbye    
    - action_restart

# interactive_story_create_stream_no_workspace_found 2
* greet: hello
    - utter_greet
* name{"name": "bilel ben brahim"}
    - slot{"name": "bilel ben brahim"}
    - utter_ask_howcanhelp
* create_stream: i would like to add my stream
    - create_stream_form
    - form{"name": "create_stream_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "504"}
    - slot{"org_id": "504"}
    - form: create_stream_form
    - slot{"org_id": "504"}
* create_workspace: i want to add the workspace
    - create_workspace_form
    - form{"name": "create_workspace_form"}
    - slot{"requested_slot": "workspace_type"}
    - form: inform{"workspace_type": "General Workspace"}
    - slot{"workspace_type": "General Workspace"}
    - form: create_workspace_form
    - slot{"workspace_type": "General Workspace"}
    - slot{"requested_slot": "workspace_name"}
    - form: inform{"workspace_name": "serenity5"}
    - slot{"workspace_name": "serenity5"}
    - form: create_workspace_form
    - slot{"workspace_name": "serenity5"}
    - slot{"requested_slot": "workspace_description"}
    - form: inform{"workspace_description": "this a workspace with harmony"}
    - slot{"workspace_description": "this a workspace with harmony"}
    - form: create_workspace_form
    - slot{"workspace_description": "this a workspace with harmony"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: yeah
    - action_create_workspace
* create_stream: i would like to add my stream
    - create_stream_form
    - form{"name": "create_stream_form"}
    - slot{"ws_id": "608"}
    - form: create_stream_form
    - slot{"ws_id": "608"}
    - slot{"requested_slot": "stream_name"}
    - form: inform{"stream_name": "devops docker"}
    - slot{"stream_name": "devops docker"}
    - form: create_stream_form
    - slot{"stream_name": "devops docker"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* deny: no thanks
    - utter_ask_continue
* affirm: yeah
    - action_create_stream
* goodbye: goodbye
    
    - utter_goodbye    
    - action_restart

# interactive_story_create_stream_no_workspace_found 3
* greet: hello
    - utter_greet
* name{"name": "salim dridi"}
    - slot{"name": "salim dridi"}
    - utter_ask_howcanhelp
* create_stream: i would like to add my stream
    - create_stream_form
    - form{"name": "create_stream_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "709"}
    - slot{"org_id": "709"}
    - form: create_stream_form
    - slot{"org_id": "709"}
* create_workspace: i want to add the workspace
    - create_workspace_form
    - form{"name": "create_workspace_form"}
    - slot{"requested_slot": "workspace_type"}
    - form: inform{"workspace_type": "Agile Development"}
    - slot{"workspace_type": "Agile Development"}
    - form: create_workspace_form
    - slot{"workspace_type": "Agile Development"}
    - slot{"requested_slot": "workspace_name"}
    - form: inform{"workspace_name": "angular 7"}
    - slot{"workspace_name": "angular 7"}
    - form: create_workspace_form
    - slot{"workspace_name": "angular 7"}
    - slot{"requested_slot": "workspace_description"}
    - form: inform{"workspace_description": "web app using angular"}
    - slot{"workspace_description": "web app using angular"}
    - form: create_workspace_form
    - slot{"workspace_description": "web app using angular"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: yeah
    - action_create_workspace
* create_stream: i would like to add my stream
    - create_stream_form
    - form{"name": "create_stream_form"}
    - slot{"ws_id": "101"}
    - form: create_stream_form
    - slot{"ws_id": "101"}
    - slot{"requested_slot": "stream_name"}
    - form: inform{"stream_name": "first link"}
    - slot{"stream_name": "first link"}
    - form: create_stream_form
    - slot{"stream_name": "first link"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* deny: no thanks
    - utter_ask_continue
* affirm: yeah
    - action_create_stream
* goodbye: goodbye
    
    - utter_goodbye    
    - action_restart

# interactive_story_create_stream_no_workspace_found 4
* greet: hello
    - utter_greet
* name{"name": "mounir torudi"}
    - slot{"name": "mounir torudi"}
    - utter_ask_howcanhelp
* create_stream: i would like to add my stream
    - create_stream_form
    - form{"name": "create_stream_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "808"}
    - slot{"org_id": "808"}
    - form: create_stream_form
    - slot{"org_id": "808"}
* create_workspace: i want to add the workspace
    - create_workspace_form
    - form{"name": "create_workspace_form"}
    - slot{"requested_slot": "workspace_type"}
    - form: inform{"workspace_type": "Agile Development"}
    - slot{"workspace_type": "Agile Development"}
    - form: create_workspace_form
    - slot{"workspace_type": "Agile Development"}
    - slot{"requested_slot": "workspace_name"}
    - form: inform{"workspace_name": "dev branch"}
    - slot{"workspace_name": "dev branch"}
    - form: create_workspace_form
    - slot{"workspace_name": "dev branch"}
    - slot{"requested_slot": "workspace_description"}
    - form: inform{"workspace_description": "working for better solutions"}
    - slot{"workspace_description": "working for better solutions"}
    - form: create_workspace_form
    - slot{"workspace_description": "working for better solutions"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: yeah
    - action_create_workspace
* create_stream: i would like to add my stream
    - create_stream_form
    - form{"name": "create_stream_form"}
    - slot{"ws_id": "603"}
    - form: create_stream_form
    - slot{"ws_id": "603"}
    - slot{"requested_slot": "stream_name"}
    - form: inform{"stream_name": "success"}
    - slot{"stream_name": "success"}
    - form: create_stream_form
    - slot{"stream_name": "success"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* deny: no thanks
    - utter_ask_continue
* affirm: yeah
    - action_create_stream
* goodbye: goodbye
    
    - utter_goodbye    
    - action_restart

# interactive_story_create_stream_no_workspace_found 5
* greet: hello
    - utter_greet
* name{"name": "mounir torudi"}
    - slot{"name": "mounir torudi"}
    - utter_ask_howcanhelp
* create_stream: i would like to add my stream
    - create_stream_form
    - form{"name": "create_stream_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "808"}
    - slot{"org_id": "808"}
    - form: create_stream_form
    - slot{"org_id": "808"}
* create_workspace: i want to add the workspace
    - create_workspace_form
    - form{"name": "create_workspace_form"}
    - slot{"requested_slot": "workspace_type"}
    - form: inform{"workspace_type": "Agile Development"}
    - slot{"workspace_type": "Agile Development"}
    - form: create_workspace_form
    - slot{"workspace_type": "Agile Development"}
    - slot{"requested_slot": "workspace_name"}
    - form: inform{"workspace_name": "dev branch"}
    - slot{"workspace_name": "dev branch"}
    - form: create_workspace_form
    - slot{"workspace_name": "dev branch"}
    - slot{"requested_slot": "workspace_description"}
    - form: inform{"workspace_description": "working for better solutions"}
    - slot{"workspace_description": "working for better solutions"}
    - form: create_workspace_form
    - slot{"workspace_description": "working for better solutions"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: yeah
    - action_create_workspace
* create_stream: i would like to add my stream
    - create_stream_form
    - form{"name": "create_stream_form"}
    - slot{"ws_id": "603"}
    - form: create_stream_form
    - slot{"ws_id": "603"}
    - slot{"requested_slot": "stream_name"}
    - form: inform{"stream_name": "success"}
    - slot{"stream_name": "success"}
    - form: create_stream_form
    - slot{"stream_name": "success"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* deny: no thanks
    - utter_ask_continue
* affirm: yeah
    - action_create_stream
* goodbye: bye was nice talking to you
    
    - utter_goodbye    
    - action_restart

# interactive_story_create_stream_no_workspace_found 6
* greet: hello
    - utter_greet
* name{"name": "mounir torudi"}
    - slot{"name": "mounir torudi"}
    - utter_ask_howcanhelp
* create_stream: i would like to add my stream
    - create_stream_form
    - form{"name": "create_stream_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "808"}
    - slot{"org_id": "808"}
    - form: create_stream_form
    - slot{"org_id": "808"}
* create_workspace: i want to add the workspace
    - create_workspace_form
    - form{"name": "create_workspace_form"}
    - slot{"requested_slot": "workspace_type"}
    - form: inform{"workspace_type": "Agile Development"}
    - slot{"workspace_type": "Agile Development"}
    - form: create_workspace_form
    - slot{"workspace_type": "Agile Development"}
    - slot{"requested_slot": "workspace_name"}
    - form: inform{"workspace_name": "dev branch"}
    - slot{"workspace_name": "dev branch"}
    - form: create_workspace_form
    - slot{"workspace_name": "dev branch"}
    - slot{"requested_slot": "workspace_description"}
    - form: inform{"workspace_description": "working for better solutions"}
    - slot{"workspace_description": "working for better solutions"}
    - form: create_workspace_form
    - slot{"workspace_description": "working for better solutions"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: yeah
    - action_create_workspace
* create_stream: i would like to add my stream
    - create_stream_form
    - form{"name": "create_stream_form"}
    - slot{"ws_id": "603"}
    - form: create_stream_form
    - slot{"ws_id": "603"}
    - slot{"requested_slot": "stream_name"}
    - form: inform{"stream_name": "success"}
    - slot{"stream_name": "success"}
    - form: create_stream_form
    - slot{"stream_name": "success"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* deny: no thanks
    - utter_ask_continue
* affirm: that sounds good
    - action_create_stream
* goodbye: bye was nice talking to you
    
    - utter_goodbye    
    - action_restart

# interactive_story_create_task_no_workspace_found 
* greet: hello
    - utter_greet
* name{"name": "salima gafsi"}
    - slot{"name": "salima gafsi"}
    - utter_ask_howcanhelp
* create_task: adding my task in Task manager
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "107"}
    - slot{"org_id": "107"}
    - form: create_task_form
    - slot{"org_id": "107"}

* create_workspace: i want to add the workspace
    - create_workspace_form
    - form{"name": "create_workspace_form"}
    - slot{"requested_slot": "workspace_type"}
    - form: inform{"workspace_type": "General Workspace"}
    - slot{"workspace_type": "General Workspace"}
    - form: create_workspace_form
    - slot{"workspace_type": "General Workspace"}
    - slot{"requested_slot": "workspace_name"}
    - form: inform{"workspace_name": "simulation"}
    - slot{"workspace_name": "simulation"}
    - form: create_workspace_form
    - slot{"workspace_name": "simulation"}
    - slot{"requested_slot": "workspace_description"}
    - form: inform{"workspace_description": "need data for simulation"}
    - slot{"workspace_description": "need data for simulation"}
    - form: create_workspace_form
    - slot{"workspace_description": "need data for simulation"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: that sounds good
    - action_create_workspace
* create_stream: i would like to add my stream
    - create_stream_form
    - form{"name": "create_stream_form"}
    - slot{"ws_id": "478"}
    - form: create_stream_form
    - slot{"ws_id": "478"}
    - slot{"requested_slot": "stream_name"}
    - form: inform{"stream_name": "simulate"}
    - slot{"stream_name": "simulate"}
    - form: create_stream_form
    - slot{"stream_name": "simulate"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* deny: no thanks
    - utter_ask_continue
* affirm: that sounds good
    - action_create_stream
* create_task: adding my task in Task manager
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"stream_id": "8745"}
    - form: create_task_form
    - slot{"stream_id": "8745"}
    - slot{"requested_slot": "task_name"}    
* form: inform{"task_name": "Simulation Accuracy"}
    - slot{"task_name": "Simulation Accuracy"}
    - form: create_task_form
    - slot{"task_name": "Simulation Accuracy"}
    - slot{"requested_slot": "task_priority"}    
* form: inform{"task_priority": "30"}
    - slot{"task_priority": "30"}
    - form: create_task_form
    - slot{"task_priority": "30"}
* deny: no thanks
    - utter_ask_continue   
* affirm: that sounds good
    - action_create_task
* goodbye: bye was nice talking to you
    - form{"name": null}
    - utter_goodbye    
    - action_restart

# interactive_story_create_task_no_workspace_found 2
* greet: hello
    - utter_greet
* name{"name": "oussema blaili"}
    - slot{"name": "oussema blaili"}
    - utter_ask_howcanhelp
* create_task: adding my task in Task manager
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "901"}
    - slot{"org_id": "901"}
    - form: create_task_form
    - slot{"org_id": "901"}

* create_workspace: i want to add the workspace
    - create_workspace_form
    - form{"name": "create_workspace_form"}
    - slot{"requested_slot": "workspace_type"}
    - form: inform{"workspace_type": "Agile Development"}
    - slot{"workspace_type": "Agile Development"}
    - form: create_workspace_form
    - slot{"workspace_type": "Agile Development"}
    - slot{"requested_slot": "workspace_name"}
    - form: inform{"workspace_name": "serenity3"}
    - slot{"workspace_name": "serenity3"}
    - form: create_workspace_form
    - slot{"workspace_name": "serenity3"}
    - slot{"requested_slot": "workspace_description"}
    - form: inform{"workspace_description": "for more serenity"}
    - slot{"workspace_description": "for more serenity"}
    - form: create_workspace_form
    - slot{"workspace_description": "for more serenity"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: that sounds good
    - action_create_workspace
* create_stream: i would like to add my stream
    - create_stream_form
    - form{"name": "create_stream_form"}
    - slot{"ws_id": "333"}
    - form: create_stream_form
    - slot{"ws_id": "333"}
    - slot{"requested_slot": "stream_name"}
    - form: inform{"stream_name": "boiling"}
    - slot{"stream_name": "boiling"}
    - form: create_stream_form
    - slot{"stream_name": "boiling"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* deny: no thanks
    - utter_ask_continue
* affirm: that sounds good
    - action_create_stream
* create_task: adding my task in Task manager
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"stream_id": "1900"}
    - form: create_task_form
    - slot{"stream_id": "1900"}
    - slot{"requested_slot": "task_name"}    
* form: inform{"task_name": "buttons design"}
    - slot{"task_name": "buttons design"}
    - form: create_task_form
    - slot{"task_name": "buttons design"}
    - slot{"requested_slot": "task_priority"}    
* form: inform{"task_priority": "30"}
    - slot{"task_priority": "30"}
    - form: create_task_form
    - slot{"task_priority": "30"}
* deny: no thanks
    - utter_ask_continue   
* affirm: that sounds good
    - action_create_task
* goodbye: bye was nice talking to you
    - form{"name": null}
    - utter_goodbye    
    - action_restart

# interactive_story_create_task_no_workspace_found 3
* greet: hello
    - utter_greet
* name{"name": "achraf ben mustapha"}
    - slot{"name": "achraf ben mustapha"}
    - utter_ask_howcanhelp
* create_task: adding my task in Task manager
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "208"}
    - slot{"org_id": "208"}
    - form: create_task_form
    - slot{"org_id": "208"}
* create_workspace: i want to add the workspace
    - create_workspace_form
    - form{"name": "create_workspace_form"}
    - slot{"requested_slot": "workspace_type"}
    - form: inform{"workspace_type": "Agile Development"}
    - slot{"workspace_type": "Agile Development"}
    - form: create_workspace_form
    - slot{"workspace_type": "Agile Development"}
    - slot{"requested_slot": "workspace_name"}
    - form: inform{"workspace_name": "organisation"}
    - slot{"workspace_name": "organisation"}
    - form: create_workspace_form
    - slot{"workspace_name": "organisation"}
    - slot{"requested_slot": "workspace_description"}
    - form: inform{"workspace_description": "dealing with apis"}
    - slot{"workspace_description": "dealing with apis"}
    - form: create_workspace_form
    - slot{"workspace_description": "dealing with apis"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: that sounds good
    - action_create_workspace
* create_stream: i would like to add my stream
    - create_stream_form
    - form{"name": "create_stream_form"}
    - slot{"ws_id": "25"}
    - form: create_stream_form
    - slot{"ws_id": "25"}
    - slot{"requested_slot": "stream_name"}
    - form: inform{"stream_name": "api weather"}
    - slot{"stream_name": "api weather"}
    - form: create_stream_form
    - slot{"stream_name": "api weather"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* deny: no thanks
    - utter_ask_continue
* affirm: that sounds good
    - action_create_stream
* create_task: adding my task in Task manager
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"stream_id": "1616"}
    - form: create_task_form
    - slot{"stream_id": "1616"}
    - slot{"requested_slot": "task_name"}    
* form: inform{"task_name": "generate bundle"}
    - slot{"task_name": "generate bundle"}
    - form: create_task_form
    - slot{"task_name": "generate bundle"}
    - slot{"requested_slot": "task_priority"}    
* form: inform{"task_priority": "20"}
    - slot{"task_priority": "20"}
    - form: create_task_form
    - slot{"task_priority": "20"}
* deny: no thanks
    - utter_ask_continue   
* affirm: that sounds good
    - action_create_task
* goodbye: bye was nice talking to you
    - form{"name": null}
    - utter_goodbye    
    - action_restart

# interactive_story_create_task_no_workspace_found 4
* greet: hello
    - utter_greet
* name{"name": "achraf ben mustapha"}
    - slot{"name": "achraf ben mustapha"}
    - utter_ask_howcanhelp
* create_task: adding my task in Task manager
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "208"}
    - slot{"org_id": "208"}
    - form: create_task_form
    - slot{"org_id": "208"}
* create_workspace: i want to add the workspace
    - create_workspace_form
    - form{"name": "create_workspace_form"}
    - slot{"requested_slot": "workspace_type"}
    - form: inform{"workspace_type": "Agile Development"}
    - slot{"workspace_type": "Agile Development"}
    - form: create_workspace_form
    - slot{"workspace_type": "Agile Development"}
    - slot{"requested_slot": "workspace_name"}
    - form: inform{"workspace_name": "organisation"}
    - slot{"workspace_name": "organisation"}
    - form: create_workspace_form
    - slot{"workspace_name": "organisation"}
    - slot{"requested_slot": "workspace_description"}
    - form: inform{"workspace_description": "dealing with apis"}
    - slot{"workspace_description": "dealing with apis"}
    - form: create_workspace_form
    - slot{"workspace_description": "dealing with apis"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: that sounds good
    - action_create_workspace
* create_stream: i would like to add my stream
    - create_stream_form
    - form{"name": "create_stream_form"}
    - slot{"ws_id": "25"}
    - form: create_stream_form
    - slot{"ws_id": "25"}
    - slot{"requested_slot": "stream_name"}
    - form: inform{"stream_name": "api weather"}
    - slot{"stream_name": "api weather"}
    - form: create_stream_form
    - slot{"stream_name": "api weather"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* deny: no thanks
    - utter_ask_continue
* affirm: that sounds good
    - action_create_stream
* create_task: adding my task in Task manager
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"stream_id": "1616"}
    - form: create_task_form
    - slot{"stream_id": "1616"}
    - slot{"requested_slot": "task_name"}    
* form: inform{"task_name": "generate bundle"}
    - slot{"task_name": "generate bundle"}
    - form: create_task_form
    - slot{"task_name": "generate bundle"}
    - slot{"requested_slot": "task_priority"}    
* form: inform{"task_priority": "20"}
    - slot{"task_priority": "20"}
    - form: create_task_form
    - slot{"task_priority": "20"}
* deny: no thanks
    - utter_ask_continue   
* affirm: that sounds good
    - action_create_task
* goodbye: bye was nice talking to you
    - form{"name": null}
    - utter_goodbye    
    - action_restart

# interactive_story_create_task_no_workspace_found 5
* greet: hello
    - utter_greet
* name{"name": "achraf ben mustapha"}
    - slot{"name": "achraf ben mustapha"}
    - utter_ask_howcanhelp
* create_task: adding my task in Task manager
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
* form: inform{"org_id": "208"}
    - slot{"org_id": "208"}
    - form: create_task_form
    - slot{"org_id": "208"}
* create_workspace: i want to add the workspace
    - create_workspace_form
    - form{"name": "create_workspace_form"}
    - slot{"requested_slot": "workspace_type"}
    - form: inform{"workspace_type": "Agile Development"}
    - slot{"workspace_type": "Agile Development"}
    - form: create_workspace_form
    - slot{"workspace_type": "Agile Development"}
    - slot{"requested_slot": "workspace_name"}
    - form: inform{"workspace_name": "organisation"}
    - slot{"workspace_name": "organisation"}
    - form: create_workspace_form
    - slot{"workspace_name": "organisation"}
    - slot{"requested_slot": "workspace_description"}
    - form: inform{"workspace_description": "dealing with apis"}
    - slot{"workspace_description": "dealing with apis"}
    - form: create_workspace_form
    - slot{"workspace_description": "dealing with apis"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: that sounds good
    - action_create_workspace
* create_stream: i would like to add my stream
    - create_stream_form
    - form{"name": "create_stream_form"}
    - slot{"ws_id": "25"}
    - form: create_stream_form
    - slot{"ws_id": "25"}
    - slot{"requested_slot": "stream_name"}
    - form: inform{"stream_name": "api weather"}
    - slot{"stream_name": "api weather"}
    - form: create_stream_form
    - slot{"stream_name": "api weather"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* deny: no thanks
    - utter_ask_continue
* affirm: that sounds good
    - action_create_stream
* create_task: adding my task in Task manager
    - create_task_form
    - form{"name": "create_task_form"}
    - slot{"stream_id": "1616"}
    - form: create_task_form
    - slot{"stream_id": "1616"}
    - slot{"requested_slot": "task_name"}    
* form: inform{"task_name": "generate bundle"}
    - slot{"task_name": "generate bundle"}
    - form: create_task_form
    - slot{"task_name": "generate bundle"}
    - slot{"requested_slot": "task_priority"}    
* form: inform{"task_priority": "20"}
    - slot{"task_priority": "20"}
    - form: create_task_form
    - slot{"task_priority": "20"}
* deny: no thanks
    - utter_ask_continue   
* affirm: that sounds good
    - action_create_task
* goodbye: bye was nice talking to you
    - form{"name": null}
    - utter_goodbye    
    - action_restart