## create task happy path 5 (C:\Users\user\AppData\Local\Temp\tmpe8mvuugi\578cdfa598914fa1acf922f22a0d46bb_test_stories.md)
* greet: hello
    - utter_greet   <!-- predicted: action_default_fallback -->
* name{"name": "mahdi"}
    - slot{"name": "mahdi"}
    - slot{"name": "mahdi"}
    - utter_ask_howcanhelp
* create_task: i want to add a new task
    - create_task_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
    - slot{"org_id": "148"}
    - slot{"org_id": "148"}
    - slot{"requested_slot": "ws_id"}
    - slot{"ws_id": "1587"}
    - slot{"ws_id": "1587"}
    - slot{"requested_slot": "stream_id"}
    - slot{"stream_id": "2271"}
    - slot{"stream_id": "2271"}
    - slot{"requested_slot": "task_name"}
    - slot{"task_name": "create nlu data"}
    - slot{"task_name": "create nlu data"}
    - slot{"requested_slot": "task_priority"}
    - slot{"task_priority": "10"}
    - slot{"task_priority": "10"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm: yes
    - action_create_task   <!-- predicted: action_default_fallback -->
* goodbye: bye
    - utter_goodbye   <!-- predicted: action_default_fallback -->
    - action_restart


## "create task" stop but continue (deny) path 1 (C:\Users\user\AppData\Local\Temp\tmpe8mvuugi\578cdfa598914fa1acf922f22a0d46bb_test_stories.md)
* greet: hello
    - utter_greet   <!-- predicted: action_default_fallback -->
* name{"name": "mahdi"}
    - slot{"name": "mahdi"}
    - slot{"name": "mahdi"}
    - utter_ask_howcanhelp
* create_task: i want to add a new task
    - create_task_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
    - slot{"org_id": "148"}
    - slot{"org_id": "148"}
    - slot{"requested_slot": "ws_id"}
    - slot{"ws_id": "1587"}
    - slot{"ws_id": "1587"}
    - slot{"requested_slot": "stream_id"}
    - slot{"stream_id": "2271"}
    - slot{"stream_id": "2271"}
    - slot{"requested_slot": "task_name"}
    - slot{"task_name": "create nlu data"}
    - slot{"task_name": "create nlu data"}
    - slot{"requested_slot": "task_priority"}
    - slot{"task_priority": "10"}
    - slot{"task_priority": "10"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny: no
    - utter_ask_continue   <!-- predicted: action_default_fallback -->
* affirm: yes
    - action_create_task   <!-- predicted: action_default_fallback -->
* goodbye: bye
    - utter_goodbye   <!-- predicted: action_default_fallback -->
    - action_restart


## "create task" stop but continue (deny) path 3 (C:\Users\user\AppData\Local\Temp\tmpe8mvuugi\578cdfa598914fa1acf922f22a0d46bb_test_stories.md)
* greet: hello
    - utter_greet   <!-- predicted: action_default_fallback -->
* name{"name": "syrine"}
    - slot{"name": "syrine"}
    - slot{"name": "syrine"}
    - utter_ask_howcanhelp
* create_task: i want to add a new task
    - create_task_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
    - slot{"org_id": "501"}
    - slot{"org_id": "501"}
    - slot{"requested_slot": "ws_id"}
    - slot{"ws_id": "4187"}
    - slot{"ws_id": "4187"}
    - slot{"requested_slot": "stream_id"}
    - slot{"stream_id": "2532"}
    - slot{"stream_id": "2532"}
    - slot{"requested_slot": "task_name"}
    - slot{"task_name": "create config"}
    - slot{"task_name": "create config"}
    - slot{"requested_slot": "task_priority"}
    - slot{"task_priority": "30"}
    - slot{"task_priority": "30"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny: no
    - utter_ask_continue   <!-- predicted: action_default_fallback -->
* affirm: yes
    - action_create_task   <!-- predicted: action_default_fallback -->
* goodbye: bye
    - utter_goodbye   <!-- predicted: action_default_fallback -->
    - action_restart


## "create task" stop but continue (deny) path 4 (C:\Users\user\AppData\Local\Temp\tmpe8mvuugi\578cdfa598914fa1acf922f22a0d46bb_test_stories.md)
* greet: hello
    - utter_greet   <!-- predicted: action_default_fallback -->
* name{"name": "omar"}
    - slot{"name": "omar"}
    - slot{"name": "omar"}
    - utter_ask_howcanhelp
* create_task: i want to add a new task
    - create_task_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
    - slot{"org_id": "201"}
    - slot{"org_id": "201"}
    - slot{"requested_slot": "ws_id"}
    - slot{"ws_id": "1787"}
    - slot{"ws_id": "1787"}
    - slot{"requested_slot": "stream_id"}
    - slot{"stream_id": "2832"}
    - slot{"stream_id": "2832"}
    - slot{"requested_slot": "task_name"}
    - slot{"task_name": "create glue scripts"}
    - slot{"task_name": "create glue scripts"}
    - slot{"requested_slot": "task_priority"}
    - slot{"task_priority": "20"}
    - slot{"task_priority": "20"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny: no
    - utter_ask_continue   <!-- predicted: action_default_fallback -->
* affirm: yes
    - action_create_task   <!-- predicted: action_default_fallback -->
* goodbye: bye
    - utter_goodbye   <!-- predicted: action_default_fallback -->
    - action_restart


## "create task" stop and really stop (deny) path 1 (C:\Users\user\AppData\Local\Temp\tmpe8mvuugi\578cdfa598914fa1acf922f22a0d46bb_test_stories.md)
* greet: hello
    - utter_greet   <!-- predicted: action_default_fallback -->
* name{"name": "mahdi"}
    - slot{"name": "mahdi"}
    - slot{"name": "mahdi"}
    - utter_ask_howcanhelp
* create_task: i want to add a new task
    - create_task_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
    - slot{"org_id": "148"}
    - slot{"org_id": "148"}
    - slot{"requested_slot": "ws_id"}
    - slot{"ws_id": "1587"}
    - slot{"ws_id": "1587"}
    - slot{"requested_slot": "stream_id"}
    - slot{"stream_id": "2271"}
    - slot{"stream_id": "2271"}
    - slot{"requested_slot": "task_name"}
    - slot{"task_name": "create nlu data"}
    - slot{"task_name": "create nlu data"}
    - slot{"requested_slot": "task_priority"}
    - slot{"task_priority": "10"}
    - slot{"task_priority": "10"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny: no
    - utter_ask_continue   <!-- predicted: action_default_fallback -->
* deny: no
    - utter_sorry   <!-- predicted: action_default_fallback -->
    - action_restart   <!-- predicted: action_default_fallback -->


## "create task" stop and really stop (deny) path 3 (C:\Users\user\AppData\Local\Temp\tmpe8mvuugi\578cdfa598914fa1acf922f22a0d46bb_test_stories.md)
* greet: hello
    - utter_greet   <!-- predicted: action_default_fallback -->
* name{"name": "syrine"}
    - slot{"name": "syrine"}
    - slot{"name": "syrine"}
    - utter_ask_howcanhelp
* create_task: i want to add new task in Task manager
    - create_task_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
    - slot{"org_id": "501"}
    - slot{"org_id": "501"}
    - slot{"requested_slot": "ws_id"}
    - slot{"ws_id": "4187"}
    - slot{"ws_id": "4187"}
    - slot{"requested_slot": "stream_id"}
    - slot{"stream_id": "2532"}
    - slot{"stream_id": "2532"}
    - slot{"requested_slot": "task_name"}
    - slot{"task_name": "create config"}
    - slot{"task_name": "create config"}
    - slot{"requested_slot": "task_priority"}
    - slot{"task_priority": "30"}
    - slot{"task_priority": "30"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny: no
    - utter_ask_continue   <!-- predicted: action_default_fallback -->
* deny: no
    - utter_sorry   <!-- predicted: action_default_fallback -->
    - action_restart   <!-- predicted: action_default_fallback -->


## "create task" stop and really stop (deny) path 4 (C:\Users\user\AppData\Local\Temp\tmpe8mvuugi\578cdfa598914fa1acf922f22a0d46bb_test_stories.md)
* greet: hello
    - utter_greet   <!-- predicted: action_default_fallback -->
* name{"name": "omar"}
    - slot{"name": "omar"}
    - slot{"name": "omar"}
    - utter_ask_howcanhelp
* create_task: i want to add new task in Task manager
    - create_task_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
    - slot{"org_id": "201"}
    - slot{"org_id": "201"}
    - slot{"requested_slot": "ws_id"}
    - slot{"ws_id": "1787"}
    - slot{"ws_id": "1787"}
    - slot{"requested_slot": "stream_id"}
    - slot{"stream_id": "2832"}
    - slot{"stream_id": "2832"}
    - slot{"requested_slot": "task_name"}
    - slot{"task_name": "create glue scripts"}
    - slot{"task_name": "create glue scripts"}
    - slot{"requested_slot": "task_priority"}
    - slot{"task_priority": "20"}
    - slot{"task_priority": "20"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny: no
    - utter_ask_continue   <!-- predicted: action_default_fallback -->
* deny: no
    - utter_sorry   <!-- predicted: action_default_fallback -->
    - action_restart   <!-- predicted: action_default_fallback -->


## say hello (C:\Users\user\AppData\Local\Temp\tmpe8mvuugi\578cdfa598914fa1acf922f22a0d46bb_test_stories.md)
* greet: hello
    - utter_greet   <!-- predicted: action_default_fallback -->


## interactive_story_1 (C:\Users\user\AppData\Local\Temp\tmpe8mvuugi\578cdfa598914fa1acf922f22a0d46bb_test_stories.md)
* greet: hello
    - utter_greet   <!-- predicted: action_default_fallback -->
* name{"name": "omar"}
    - slot{"name": "omar"}
    - slot{"name": "omar"}
    - create_task_form   <!-- predicted: utter_ask_howcanhelp -->
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
    - slot{"org_id": "548"}
    - slot{"org_id": "548"}
    - slot{"requested_slot": "ws_id"}
    - slot{"ws_id": "924"}
    - slot{"ws_id": "924"}
    - slot{"requested_slot": "stream_id"}
    - slot{"stream_id": "687"}
    - slot{"stream_id": "687"}
    - slot{"requested_slot": "task_name"}
    - slot{"task_name": "ws chatbot backbones creation"}
    - slot{"task_name": "ws chatbot backbones creation"}
    - slot{"requested_slot": "task_priority"}
    - slot{"task_priority": "30"}
    - slot{"task_priority": "30"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm: yes
    - action_create_task   <!-- predicted: action_default_fallback -->
* goodbye: bye
    - utter_goodbye   <!-- predicted: action_default_fallback -->
    - action_restart


## interactive_story_create_stream_happy_path_1 (C:\Users\user\AppData\Local\Temp\tmpe8mvuugi\578cdfa598914fa1acf922f22a0d46bb_test_stories.md)
* greet: hello
    - utter_greet   <!-- predicted: action_default_fallback -->
* name{"name": "bilel ben brahim"}
    - slot{"name": "bilel ben brahim"}
    - slot{"name": "bilel ben brahim"}
    - utter_ask_howcanhelp
* create_stream: i want to add a stream
    - create_stream_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_stream_form"}
    - slot{"requested_slot": "org_id"}
    - slot{"org_id": "358"}
    - slot{"org_id": "358"}
    - slot{"requested_slot": "ws_id"}
    - slot{"ws_id": "698"}
    - slot{"ws_id": "698"}
    - slot{"requested_slot": "stream_name"}
    - slot{"stream_name": "front-end validation"}
    - slot{"stream_name": "front-end validation"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: yes
    - action_create_stream   <!-- predicted: action_default_fallback -->
* goodbye: bye
    - utter_goodbye   <!-- predicted: action_default_fallback -->
    - action_restart


## interactive_story_create_workspace_happy_path_1 (C:\Users\user\AppData\Local\Temp\tmpe8mvuugi\578cdfa598914fa1acf922f22a0d46bb_test_stories.md)
* greet: hello
    - utter_greet   <!-- predicted: action_default_fallback -->
* name{"name": "syrine slouli"}
    - slot{"name": "syrine slouli"}
    - slot{"name": "syrine slouli"}
    - utter_ask_howcanhelp
* create_workspace: i want to add the workspace
    - create_workspace_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_workspace_form"}
    - slot{"requested_slot": "org_id"}
    - slot{"org_id": "100"}
    - slot{"org_id": "100"}
    - slot{"requested_slot": "workspace_type"}
    - slot{"workspace_type": "General Workspace"}
    - slot{"workspace_type": "General Workspace"}
    - slot{"requested_slot": "workspace_name"}
    - slot{"workspace_name": "image processing and analysis"}
    - slot{"workspace_name": "image processing and analysis"}
    - slot{"requested_slot": "workspace_description"}
    - slot{"workspace_description": "creating a new workspace type"}
    - slot{"workspace_description": "creating a new workspace type"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: yes
    - action_create_workspace   <!-- predicted: action_default_fallback -->
* goodbye: goodbye
    - utter_goodbye   <!-- predicted: action_default_fallback -->
    - action_restart


## interactive_story_create_workspace_happy_path_3 (C:\Users\user\AppData\Local\Temp\tmpe8mvuugi\578cdfa598914fa1acf922f22a0d46bb_test_stories.md)
* greet: hello
    - utter_greet   <!-- predicted: action_default_fallback -->
* name{"name": "mahdi ben ali"}
    - slot{"name": "mahdi ben ali"}
    - slot{"name": "mahdi ben ali"}
    - utter_ask_howcanhelp
* create_workspace: i want to add the workspace
    - create_workspace_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_workspace_form"}
    - slot{"requested_slot": "org_id"}
    - slot{"org_id": "548"}
    - slot{"org_id": "548"}
    - slot{"requested_slot": "workspace_type"}
    - slot{"workspace_type": "Agile Development"}
    - slot{"workspace_type": "Agile Development"}
    - slot{"requested_slot": "workspace_name"}
    - slot{"workspace_name": "Serenity-test-target"}
    - slot{"workspace_name": "Serenity-test-target"}
    - slot{"requested_slot": "workspace_description"}
    - slot{"workspace_description": "Test workspace"}
    - slot{"workspace_description": "Test workspace"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: yes
    - action_create_workspace   <!-- predicted: action_default_fallback -->
* goodbye: goodbye
    - utter_goodbye   <!-- predicted: action_default_fallback -->
    - action_restart


## interactive_story_create_task_no_stream_found (C:\Users\user\AppData\Local\Temp\tmpe8mvuugi\578cdfa598914fa1acf922f22a0d46bb_test_stories.md)
* greet: hello
    - utter_greet   <!-- predicted: action_default_fallback -->
* name{"name": "melek"}
    - slot{"name": "melek"}
    - slot{"name": "melek"}
    - utter_ask_howcanhelp
* create_task: i want to add new task in Task manager
    - create_task_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
    - slot{"org_id": "107"}
    - slot{"org_id": "107"}
    - slot{"requested_slot": "ws_id"}
    - slot{"ws_id": "604"}
    - slot{"ws_id": "604"}
* form: change_path: can i change the path ?
    - form: utter_change_path   <!-- predicted: create_task_form -->
    - form: action_listen   <!-- predicted: action_default_fallback -->
* form: create_stream: i want to add a stream
    - form: create_stream_form   <!-- predicted: create_task_form -->
    - form{"name": "create_stream_form"}
    - slot{"requested_slot": "stream_name"}
    - slot{"stream_name": "training"}
    - slot{"stream_name": "training"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: yes
    - action_create_stream   <!-- predicted: action_default_fallback -->
* create_task: i want to add new task in Task manager
    - create_task_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_task_form"}
    - slot{"stream_id": "1407"}
    - slot{"stream_id": "1407"}
    - slot{"requested_slot": "task_name"}
    - slot{"task_name": "test for test"}
    - slot{"task_name": "test for test"}
    - slot{"requested_slot": "task_priority"}
    - slot{"task_priority": "10"}
    - slot{"task_priority": "10"}
* form: deny: no
    - form: utter_ask_continue   <!-- predicted: create_task_form -->
    - form: action_listen   <!-- predicted: action_default_fallback -->
* form: affirm: yeah
    - form: action_create_task   <!-- predicted: create_task_form -->
    - form: action_listen   <!-- predicted: action_default_fallback -->
* form: goodbye: goodbye
    - form{"name": null}
    - form{"name": null}
    - utter_goodbye   <!-- predicted: action_default_fallback -->
    - action_restart


## interactive_story_create_task_no_stream_found 2 (C:\Users\user\AppData\Local\Temp\tmpe8mvuugi\578cdfa598914fa1acf922f22a0d46bb_test_stories.md)
* greet: hello
    - utter_greet   <!-- predicted: action_default_fallback -->
* name{"name": "bilel"}
    - slot{"name": "bilel"}
    - slot{"name": "bilel"}
    - utter_ask_howcanhelp
* create_task: i want to add new task in Task manager
    - create_task_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
    - slot{"org_id": "508"}
    - slot{"org_id": "508"}
    - slot{"requested_slot": "ws_id"}
    - slot{"ws_id": "1006"}
    - slot{"ws_id": "1006"}
* form: change_path: can i change the path ?
    - form: utter_change_path   <!-- predicted: create_task_form -->
    - form: action_listen   <!-- predicted: action_default_fallback -->
* form: create_stream: i want to add a stream
    - form: create_stream_form   <!-- predicted: create_task_form -->
    - form{"name": "create_stream_form"}
    - slot{"requested_slot": "stream_name"}
    - slot{"stream_name": "verfication done"}
    - slot{"stream_name": "verfication done"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: yeah
    - action_create_stream   <!-- predicted: action_default_fallback -->
* create_task: i want to add new task in Task manager
    - create_task_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_task_form"}
    - slot{"stream_id": "1207"}
    - slot{"stream_id": "1207"}
    - slot{"requested_slot": "task_name"}
    - slot{"task_name": "last step"}
    - slot{"task_name": "last step"}
    - slot{"requested_slot": "task_priority"}
    - slot{"task_priority": "20"}
    - slot{"task_priority": "20"}
* form: deny: no
    - form: utter_ask_continue   <!-- predicted: create_task_form -->
    - form: action_listen   <!-- predicted: action_default_fallback -->
* form: affirm: yeah
    - form: action_create_task   <!-- predicted: create_task_form -->
    - form: action_listen   <!-- predicted: action_default_fallback -->
* form: goodbye: goodbye
    - form: utter_goodbye   <!-- predicted: create_task_form -->
    - form{"name": null}
    - action_restart


## say goodbye (C:\Users\user\AppData\Local\Temp\tmpe8mvuugi\578cdfa598914fa1acf922f22a0d46bb_test_stories.md)
* goodbye: bye
    - utter_goodbye   <!-- predicted: action_default_fallback -->
    - action_listen   <!-- predicted: action_restart -->


## interactive_story_create_task_no_stream_found 3 (C:\Users\user\AppData\Local\Temp\tmpe8mvuugi\578cdfa598914fa1acf922f22a0d46bb_test_stories.md)
* greet: hello
    - utter_greet   <!-- predicted: action_default_fallback -->
* name{"name": "ahmed jlassi"}
    - slot{"name": "ahmed jlassi"}
    - slot{"name": "ahmed jlassi"}
    - utter_ask_howcanhelp
* create_task: i want to add new task in Task manager
    - create_task_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
    - slot{"org_id": "598"}
    - slot{"org_id": "598"}
    - slot{"requested_slot": "ws_id"}
    - slot{"ws_id": "409"}
    - slot{"ws_id": "409"}
* form: change_path: can i change the path ?
    - form: utter_change_path   <!-- predicted: create_task_form -->
    - form: action_listen   <!-- predicted: action_default_fallback -->
* form: create_stream: i want to add a stream
    - form: create_stream_form   <!-- predicted: create_task_form -->
    - form{"name": "create_stream_form"}
    - slot{"requested_slot": "stream_name"}
    - slot{"stream_name": "second strategy"}
    - slot{"stream_name": "second strategy"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: yeah
    - action_create_stream   <!-- predicted: action_default_fallback -->
* create_task: i want to add new task in Task manager
    - create_task_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_task_form"}
    - slot{"stream_id": "1587"}
    - slot{"stream_id": "1587"}
    - slot{"requested_slot": "task_name"}
    - slot{"task_name": "from scratch"}
    - slot{"task_name": "from scratch"}
    - slot{"requested_slot": "task_priority"}
    - slot{"task_priority": "30"}
    - slot{"task_priority": "30"}
* form: deny: no
    - form: utter_ask_continue   <!-- predicted: create_task_form -->
    - form: action_listen   <!-- predicted: action_default_fallback -->
* form: affirm: yeah
    - form: action_create_task   <!-- predicted: create_task_form -->
    - form: action_listen   <!-- predicted: action_default_fallback -->
* form: goodbye: goodbye
    - form{"name": null}
    - utter_goodbye   <!-- predicted: action_default_fallback -->
    - action_restart


## interactive_story_create_task_no_stream_found 4 (C:\Users\user\AppData\Local\Temp\tmpe8mvuugi\578cdfa598914fa1acf922f22a0d46bb_test_stories.md)
* greet: hello
    - utter_greet   <!-- predicted: action_default_fallback -->
* name{"name": "ahmed jlassi"}
    - slot{"name": "ahmed jlassi"}
    - slot{"name": "ahmed jlassi"}
    - utter_ask_howcanhelp
* create_task: i want to add new task in Task manager
    - create_task_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
    - slot{"org_id": "598"}
    - slot{"org_id": "598"}
    - slot{"requested_slot": "ws_id"}
    - slot{"ws_id": "409"}
    - slot{"ws_id": "409"}
* form: create_stream: i want to add a stream
    - form: create_stream_form   <!-- predicted: create_task_form -->
    - form{"name": "create_stream_form"}
    - slot{"requested_slot": "stream_name"}
    - slot{"stream_name": "second strategy"}
    - slot{"stream_name": "second strategy"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: yeah
    - action_create_stream   <!-- predicted: action_default_fallback -->
* create_task: i want to add new task in Task manager
    - create_task_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_task_form"}
    - slot{"stream_id": "1587"}
    - slot{"stream_id": "1587"}
    - slot{"requested_slot": "task_name"}
    - slot{"task_name": "from scratch"}
    - slot{"task_name": "from scratch"}
    - slot{"requested_slot": "task_priority"}
    - slot{"task_priority": "30"}
    - slot{"task_priority": "30"}
* form: deny: no thanks
    - form: utter_ask_continue   <!-- predicted: create_task_form -->
    - form: action_listen   <!-- predicted: action_default_fallback -->
* form: affirm: yeah
    - form: action_create_task   <!-- predicted: create_task_form -->
    - form: action_listen   <!-- predicted: action_default_fallback -->
* form: goodbye: goodbye
    - form{"name": null}
    - utter_goodbye   <!-- predicted: action_default_fallback -->
    - action_restart


## interactive_story_create_task_no_stream_found 5 (C:\Users\user\AppData\Local\Temp\tmpe8mvuugi\578cdfa598914fa1acf922f22a0d46bb_test_stories.md)
* greet: hello
    - utter_greet   <!-- predicted: action_default_fallback -->
* name{"name": "ahmed jlassi"}
    - slot{"name": "ahmed jlassi"}
    - slot{"name": "ahmed jlassi"}
    - utter_ask_howcanhelp
* create_task: adding my task in Task manager
    - create_task_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
    - slot{"org_id": "598"}
    - slot{"org_id": "598"}
    - slot{"requested_slot": "ws_id"}
    - slot{"ws_id": "409"}
    - slot{"ws_id": "409"}
* form: create_stream: i want to add a stream
    - form: create_stream_form   <!-- predicted: create_task_form -->
    - form{"name": "create_stream_form"}
    - slot{"requested_slot": "stream_name"}
    - slot{"stream_name": "second strategy"}
    - slot{"stream_name": "second strategy"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: yeah
    - action_create_stream   <!-- predicted: action_default_fallback -->
* create_task: adding my task in Task manager
    - create_task_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_task_form"}
    - slot{"stream_id": "1587"}
    - slot{"stream_id": "1587"}
    - slot{"requested_slot": "task_name"}
    - slot{"task_name": "from scratch"}
    - slot{"task_name": "from scratch"}
    - slot{"requested_slot": "task_priority"}
    - slot{"task_priority": "30"}
    - slot{"task_priority": "30"}
* form: deny: no thanks
    - form: utter_ask_continue   <!-- predicted: create_task_form -->
    - form: action_listen   <!-- predicted: action_default_fallback -->
* form: affirm: yeah
    - form: action_create_task   <!-- predicted: create_task_form -->
    - form: action_listen   <!-- predicted: action_default_fallback -->
* form: goodbye: goodbye
    - form{"name": null}
    - utter_goodbye   <!-- predicted: action_default_fallback -->
    - action_restart


## interactive_story_create_stream_no_workspace_found (C:\Users\user\AppData\Local\Temp\tmpe8mvuugi\578cdfa598914fa1acf922f22a0d46bb_test_stories.md)
* greet: hello
    - utter_greet   <!-- predicted: action_default_fallback -->
* name{"name": "ahmed jlassi"}
    - slot{"name": "ahmed jlassi"}
    - slot{"name": "ahmed jlassi"}
    - utter_ask_howcanhelp
* create_stream: i want to add a stream
    - create_stream_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_stream_form"}
    - slot{"requested_slot": "org_id"}
    - slot{"org_id": "358"}
    - slot{"org_id": "358"}
* form: create_workspace: i want to add the workspace
    - form: create_workspace_form   <!-- predicted: create_stream_form -->
    - form{"name": "create_workspace_form"}
    - slot{"requested_slot": "workspace_type"}
    - slot{"workspace_type": "General Workspace"}
    - slot{"workspace_type": "General Workspace"}
    - slot{"requested_slot": "workspace_name"}
    - slot{"workspace_name": "image processing and analysis"}
    - slot{"workspace_name": "image processing and analysis"}
    - slot{"requested_slot": "workspace_description"}
    - slot{"workspace_description": "creating a new workspace type"}
    - slot{"workspace_description": "creating a new workspace type"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: yeah
    - action_create_workspace   <!-- predicted: action_default_fallback -->
* create_stream: i want to add a stream
    - create_stream_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_stream_form"}
    - slot{"ws_id": "358"}
    - slot{"ws_id": "358"}
    - slot{"requested_slot": "stream_name"}
    - slot{"stream_name": "front-end validation"}
    - slot{"stream_name": "front-end validation"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* deny: no thanks
    - utter_ask_continue   <!-- predicted: action_default_fallback -->
* affirm: yeah
    - action_create_stream   <!-- predicted: action_default_fallback -->
* goodbye: goodbye
    - utter_goodbye   <!-- predicted: action_default_fallback -->
    - action_restart


## interactive_story_create_stream_no_workspace_found 2 (C:\Users\user\AppData\Local\Temp\tmpe8mvuugi\578cdfa598914fa1acf922f22a0d46bb_test_stories.md)
* greet: hello
    - utter_greet   <!-- predicted: action_default_fallback -->
* name{"name": "bilel ben brahim"}
    - slot{"name": "bilel ben brahim"}
    - slot{"name": "bilel ben brahim"}
    - utter_ask_howcanhelp
* create_stream: i would like to add my stream
    - create_stream_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_stream_form"}
    - slot{"requested_slot": "org_id"}
    - slot{"org_id": "504"}
    - slot{"org_id": "504"}
* form: create_workspace: i want to add the workspace
    - form: create_workspace_form   <!-- predicted: create_stream_form -->
    - form{"name": "create_workspace_form"}
    - slot{"requested_slot": "workspace_type"}
    - slot{"workspace_type": "General Workspace"}
    - slot{"workspace_type": "General Workspace"}
    - slot{"requested_slot": "workspace_name"}
    - slot{"workspace_name": "serenity5"}
    - slot{"workspace_name": "serenity5"}
    - slot{"requested_slot": "workspace_description"}
    - slot{"workspace_description": "this a workspace with harmony"}
    - slot{"workspace_description": "this a workspace with harmony"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: yeah
    - action_create_workspace   <!-- predicted: action_default_fallback -->
* create_stream: i would like to add my stream
    - create_stream_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_stream_form"}
    - slot{"ws_id": "608"}
    - slot{"ws_id": "608"}
    - slot{"requested_slot": "stream_name"}
    - slot{"stream_name": "devops docker"}
    - slot{"stream_name": "devops docker"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* deny: no thanks
    - utter_ask_continue   <!-- predicted: action_default_fallback -->
* affirm: yeah
    - action_create_stream   <!-- predicted: action_default_fallback -->
* goodbye: goodbye
    - utter_goodbye   <!-- predicted: action_default_fallback -->
    - action_restart


## interactive_story_create_stream_no_workspace_found 3 (C:\Users\user\AppData\Local\Temp\tmpe8mvuugi\578cdfa598914fa1acf922f22a0d46bb_test_stories.md)
* greet: hello
    - utter_greet   <!-- predicted: action_default_fallback -->
* name{"name": "salim dridi"}
    - slot{"name": "salim dridi"}
    - slot{"name": "salim dridi"}
    - utter_ask_howcanhelp
* create_stream: i would like to add my stream
    - create_stream_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_stream_form"}
    - slot{"requested_slot": "org_id"}
    - slot{"org_id": "709"}
    - slot{"org_id": "709"}
* form: create_workspace: i want to add the workspace
    - form: create_workspace_form   <!-- predicted: create_stream_form -->
    - form{"name": "create_workspace_form"}
    - slot{"requested_slot": "workspace_type"}
    - slot{"workspace_type": "Agile Development"}
    - slot{"workspace_type": "Agile Development"}
    - slot{"requested_slot": "workspace_name"}
    - slot{"workspace_name": "angular 7"}
    - slot{"workspace_name": "angular 7"}
    - slot{"requested_slot": "workspace_description"}
    - slot{"workspace_description": "web app using angular"}
    - slot{"workspace_description": "web app using angular"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: yeah
    - action_create_workspace   <!-- predicted: action_default_fallback -->
* create_stream: i would like to add my stream
    - create_stream_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_stream_form"}
    - slot{"ws_id": "101"}
    - slot{"ws_id": "101"}
    - slot{"requested_slot": "stream_name"}
    - slot{"stream_name": "first link"}
    - slot{"stream_name": "first link"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* deny: no thanks
    - utter_ask_continue   <!-- predicted: action_default_fallback -->
* affirm: yeah
    - action_create_stream   <!-- predicted: action_default_fallback -->
* goodbye: goodbye
    - utter_goodbye   <!-- predicted: action_default_fallback -->
    - action_restart


## interactive_story_create_stream_no_workspace_found 5 (C:\Users\user\AppData\Local\Temp\tmpe8mvuugi\578cdfa598914fa1acf922f22a0d46bb_test_stories.md)
* greet: hello
    - utter_greet   <!-- predicted: action_default_fallback -->
* name{"name": "mounir torudi"}
    - slot{"name": "mounir torudi"}
    - slot{"name": "mounir torudi"}
    - utter_ask_howcanhelp
* create_stream: i would like to add my stream
    - create_stream_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_stream_form"}
    - slot{"requested_slot": "org_id"}
    - slot{"org_id": "808"}
    - slot{"org_id": "808"}
* form: create_workspace: i want to add the workspace
    - form: create_workspace_form   <!-- predicted: create_stream_form -->
    - form{"name": "create_workspace_form"}
    - slot{"requested_slot": "workspace_type"}
    - slot{"workspace_type": "Agile Development"}
    - slot{"workspace_type": "Agile Development"}
    - slot{"requested_slot": "workspace_name"}
    - slot{"workspace_name": "dev branch"}
    - slot{"workspace_name": "dev branch"}
    - slot{"requested_slot": "workspace_description"}
    - slot{"workspace_description": "working for better solutions"}
    - slot{"workspace_description": "working for better solutions"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: yeah
    - action_create_workspace   <!-- predicted: action_default_fallback -->
* create_stream: i would like to add my stream
    - create_stream_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_stream_form"}
    - slot{"ws_id": "603"}
    - slot{"ws_id": "603"}
    - slot{"requested_slot": "stream_name"}
    - slot{"stream_name": "success"}
    - slot{"stream_name": "success"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* deny: no thanks
    - utter_ask_continue   <!-- predicted: action_default_fallback -->
* affirm: yeah
    - action_create_stream   <!-- predicted: action_default_fallback -->
* goodbye: bye was nice talking to you
    - utter_goodbye   <!-- predicted: action_default_fallback -->
    - action_restart


## interactive_story_create_stream_no_workspace_found 6 (C:\Users\user\AppData\Local\Temp\tmpe8mvuugi\578cdfa598914fa1acf922f22a0d46bb_test_stories.md)
* greet: hello
    - utter_greet   <!-- predicted: action_default_fallback -->
* name{"name": "mounir torudi"}
    - slot{"name": "mounir torudi"}
    - slot{"name": "mounir torudi"}
    - utter_ask_howcanhelp
* create_stream: i would like to add my stream
    - create_stream_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_stream_form"}
    - slot{"requested_slot": "org_id"}
    - slot{"org_id": "808"}
    - slot{"org_id": "808"}
* form: create_workspace: i want to add the workspace
    - form: create_workspace_form   <!-- predicted: create_stream_form -->
    - form{"name": "create_workspace_form"}
    - slot{"requested_slot": "workspace_type"}
    - slot{"workspace_type": "Agile Development"}
    - slot{"workspace_type": "Agile Development"}
    - slot{"requested_slot": "workspace_name"}
    - slot{"workspace_name": "dev branch"}
    - slot{"workspace_name": "dev branch"}
    - slot{"requested_slot": "workspace_description"}
    - slot{"workspace_description": "working for better solutions"}
    - slot{"workspace_description": "working for better solutions"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: yeah
    - action_create_workspace   <!-- predicted: action_default_fallback -->
* create_stream: i would like to add my stream
    - create_stream_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_stream_form"}
    - slot{"ws_id": "603"}
    - slot{"ws_id": "603"}
    - slot{"requested_slot": "stream_name"}
    - slot{"stream_name": "success"}
    - slot{"stream_name": "success"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* deny: no thanks
    - utter_ask_continue   <!-- predicted: action_default_fallback -->
* affirm: that sounds good
    - action_create_stream   <!-- predicted: action_default_fallback -->
* goodbye: bye was nice talking to you
    - utter_goodbye   <!-- predicted: action_default_fallback -->
    - action_restart


## bot challenge (C:\Users\user\AppData\Local\Temp\tmpe8mvuugi\578cdfa598914fa1acf922f22a0d46bb_test_stories.md)
* bot_challenge: are you a bot?
    - utter_iamabot   <!-- predicted: action_default_fallback -->


## interactive_story_create_task_no_workspace_found (C:\Users\user\AppData\Local\Temp\tmpe8mvuugi\578cdfa598914fa1acf922f22a0d46bb_test_stories.md)
* greet: hello
    - utter_greet   <!-- predicted: action_default_fallback -->
* name{"name": "salima gafsi"}
    - slot{"name": "salima gafsi"}
    - slot{"name": "salima gafsi"}
    - utter_ask_howcanhelp
* create_task: adding my task in Task manager
    - create_task_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
    - slot{"org_id": "107"}
    - slot{"org_id": "107"}
* form: create_workspace: i want to add the workspace
    - form: create_workspace_form   <!-- predicted: create_task_form -->
    - form{"name": "create_workspace_form"}
    - slot{"requested_slot": "workspace_type"}
    - slot{"workspace_type": "General Workspace"}
    - slot{"workspace_type": "General Workspace"}
    - slot{"requested_slot": "workspace_name"}
    - slot{"workspace_name": "simulation"}
    - slot{"workspace_name": "simulation"}
    - slot{"requested_slot": "workspace_description"}
    - slot{"workspace_description": "need data for simulation"}
    - slot{"workspace_description": "need data for simulation"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: that sounds good
    - action_create_workspace   <!-- predicted: action_default_fallback -->
* create_stream: i would like to add my stream
    - create_stream_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_stream_form"}
    - slot{"ws_id": "478"}
    - slot{"ws_id": "478"}
    - slot{"requested_slot": "stream_name"}
    - slot{"stream_name": "simulate"}
    - slot{"stream_name": "simulate"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* deny: no thanks
    - utter_ask_continue   <!-- predicted: action_default_fallback -->
* affirm: that sounds good
    - action_create_stream   <!-- predicted: action_default_fallback -->
* create_task: adding my task in Task manager
    - create_task_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_task_form"}
    - slot{"stream_id": "8745"}
    - slot{"stream_id": "8745"}
    - slot{"requested_slot": "task_name"}
    - slot{"task_name": "Simulation Accuracy"}
    - slot{"task_name": "Simulation Accuracy"}
    - slot{"requested_slot": "task_priority"}
    - slot{"task_priority": "30"}
    - slot{"task_priority": "30"}
* form: deny: no thanks
    - form: utter_ask_continue   <!-- predicted: create_task_form -->
    - form: action_listen   <!-- predicted: action_default_fallback -->
* form: affirm: that sounds good
    - form: action_create_task   <!-- predicted: create_task_form -->
    - form: action_listen   <!-- predicted: action_default_fallback -->
* form: goodbye: bye was nice talking to you
    - form{"name": null}
    - utter_goodbye   <!-- predicted: action_default_fallback -->
    - action_restart


## interactive_story_create_task_no_workspace_found 2 (C:\Users\user\AppData\Local\Temp\tmpe8mvuugi\578cdfa598914fa1acf922f22a0d46bb_test_stories.md)
* greet: hello
    - utter_greet   <!-- predicted: action_default_fallback -->
* name{"name": "oussema blaili"}
    - slot{"name": "oussema blaili"}
    - slot{"name": "oussema blaili"}
    - utter_ask_howcanhelp
* create_task: adding my task in Task manager
    - create_task_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
    - slot{"org_id": "901"}
    - slot{"org_id": "901"}
* form: create_workspace: i want to add the workspace
    - form: create_workspace_form   <!-- predicted: create_task_form -->
    - form{"name": "create_workspace_form"}
    - slot{"requested_slot": "workspace_type"}
    - slot{"workspace_type": "Agile Development"}
    - slot{"workspace_type": "Agile Development"}
    - slot{"requested_slot": "workspace_name"}
    - slot{"workspace_name": "serenity3"}
    - slot{"workspace_name": "serenity3"}
    - slot{"requested_slot": "workspace_description"}
    - slot{"workspace_description": "for more serenity"}
    - slot{"workspace_description": "for more serenity"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: that sounds good
    - action_create_workspace   <!-- predicted: action_default_fallback -->
* create_stream: i would like to add my stream
    - create_stream_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_stream_form"}
    - slot{"ws_id": "333"}
    - slot{"ws_id": "333"}
    - slot{"requested_slot": "stream_name"}
    - slot{"stream_name": "boiling"}
    - slot{"stream_name": "boiling"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* deny: no thanks
    - utter_ask_continue   <!-- predicted: action_default_fallback -->
* affirm: that sounds good
    - action_create_stream   <!-- predicted: action_default_fallback -->
* create_task: adding my task in Task manager
    - create_task_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_task_form"}
    - slot{"stream_id": "1900"}
    - slot{"stream_id": "1900"}
    - slot{"requested_slot": "task_name"}
    - slot{"task_name": "buttons design"}
    - slot{"task_name": "buttons design"}
    - slot{"requested_slot": "task_priority"}
    - slot{"task_priority": "30"}
    - slot{"task_priority": "30"}
* form: deny: no thanks
    - form: utter_ask_continue   <!-- predicted: create_task_form -->
    - form: action_listen   <!-- predicted: action_default_fallback -->
* form: affirm: that sounds good
    - form: action_create_task   <!-- predicted: create_task_form -->
    - form: action_listen   <!-- predicted: action_default_fallback -->
* form: goodbye: bye was nice talking to you
    - form{"name": null}
    - utter_goodbye   <!-- predicted: action_default_fallback -->
    - action_restart


## interactive_story_create_task_no_workspace_found 3 (C:\Users\user\AppData\Local\Temp\tmpe8mvuugi\578cdfa598914fa1acf922f22a0d46bb_test_stories.md)
* greet: hello
    - utter_greet   <!-- predicted: action_default_fallback -->
* name{"name": "achraf ben mustapha"}
    - slot{"name": "achraf ben mustapha"}
    - slot{"name": "achraf ben mustapha"}
    - utter_ask_howcanhelp
* create_task: adding my task in Task manager
    - create_task_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
    - slot{"org_id": "208"}
    - slot{"org_id": "208"}
* form: create_workspace: i want to add the workspace
    - form: create_workspace_form   <!-- predicted: create_task_form -->
    - form{"name": "create_workspace_form"}
    - slot{"requested_slot": "workspace_type"}
    - slot{"workspace_type": "Agile Development"}
    - slot{"workspace_type": "Agile Development"}
    - slot{"requested_slot": "workspace_name"}
    - slot{"workspace_name": "organisation"}
    - slot{"workspace_name": "organisation"}
    - slot{"requested_slot": "workspace_description"}
    - slot{"workspace_description": "dealing with apis"}
    - slot{"workspace_description": "dealing with apis"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* affirm: that sounds good
    - action_create_workspace   <!-- predicted: action_default_fallback -->
* create_stream: i would like to add my stream
    - create_stream_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_stream_form"}
    - slot{"ws_id": "25"}
    - slot{"ws_id": "25"}
    - slot{"requested_slot": "stream_name"}
    - slot{"stream_name": "api weather"}
    - slot{"stream_name": "api weather"}
    - form{"name": null}
    - slot{"requested_slot": "null"}
* deny: no thanks
    - utter_ask_continue   <!-- predicted: action_default_fallback -->
* affirm: that sounds good
    - action_create_stream   <!-- predicted: action_default_fallback -->
* create_task: adding my task in Task manager
    - create_task_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_task_form"}
    - slot{"stream_id": "1616"}
    - slot{"stream_id": "1616"}
    - slot{"requested_slot": "task_name"}
    - slot{"task_name": "generate bundle"}
    - slot{"task_name": "generate bundle"}
    - slot{"requested_slot": "task_priority"}
    - slot{"task_priority": "20"}
    - slot{"task_priority": "20"}
* form: deny: no thanks
    - form: utter_ask_continue   <!-- predicted: create_task_form -->
    - form: action_listen   <!-- predicted: action_default_fallback -->
* form: affirm: that sounds good
    - form: action_create_task   <!-- predicted: create_task_form -->
    - form: action_listen   <!-- predicted: action_default_fallback -->
* form: goodbye: bye was nice talking to you
    - form{"name": null}
    - utter_goodbye   <!-- predicted: action_default_fallback -->
    - action_restart


## interactive_story_2 (C:\Users\user\AppData\Local\Temp\tmpe8mvuugi\578cdfa598914fa1acf922f22a0d46bb_test_stories.md)
* greet: hello
    - utter_greet   <!-- predicted: action_default_fallback -->
* name{"name": "nada"}
    - slot{"name": "nada"}
    - slot{"name": "nada"}
    - utter_ask_howcanhelp
* create_task: i want to add a new task
    - create_task_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
    - slot{"org_id": "548"}
    - slot{"org_id": "548"}
    - slot{"requested_slot": "ws_id"}
    - slot{"ws_id": "1287"}
    - slot{"ws_id": "1287"}
    - slot{"requested_slot": "stream_id"}
    - slot{"stream_id": "1280"}
    - slot{"stream_id": "1280"}
    - slot{"requested_slot": "task_name"}
    - slot{"task_name": "action create task with chatbot"}
    - slot{"task_name": "action create task with chatbot"}
    - slot{"requested_slot": "task_priority"}
    - slot{"task_priority": "20"}
    - slot{"task_priority": "20"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm: yes
    - action_create_task   <!-- predicted: action_default_fallback -->
* goodbye: bye
    - utter_goodbye   <!-- predicted: action_default_fallback -->
    - action_restart


## create task happy path 1 (C:\Users\user\AppData\Local\Temp\tmpe8mvuugi\578cdfa598914fa1acf922f22a0d46bb_test_stories.md)
* greet: hello
    - utter_greet   <!-- predicted: action_default_fallback -->
* name{"name": "jasser"}
    - slot{"name": "jasser"}
    - slot{"name": "jasser"}
    - utter_ask_howcanhelp
* create_task: i want to add a new task
    - create_task_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
    - slot{"org_id": "548"}
    - slot{"org_id": "548"}
    - slot{"requested_slot": "ws_id"}
    - slot{"ws_id": "1287"}
    - slot{"ws_id": "1287"}
    - slot{"requested_slot": "stream_id"}
    - slot{"stream_id": "1281"}
    - slot{"stream_id": "1281"}
    - slot{"requested_slot": "task_name"}
    - slot{"task_name": "bot testing"}
    - slot{"task_name": "bot testing"}
    - slot{"requested_slot": "task_priority"}
    - slot{"task_priority": "30"}
    - slot{"task_priority": "30"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm: yes
    - action_create_task   <!-- predicted: action_default_fallback -->
* goodbye: bye
    - utter_goodbye   <!-- predicted: action_default_fallback -->
    - action_restart


## create task happy path 3 (C:\Users\user\AppData\Local\Temp\tmpe8mvuugi\578cdfa598914fa1acf922f22a0d46bb_test_stories.md)
* greet: hello
    - utter_greet   <!-- predicted: action_default_fallback -->
* name{"name": "mahdi"}
    - slot{"name": "mahdi"}
    - slot{"name": "mahdi"}
    - utter_ask_howcanhelp
* create_task: i want to add a new task
    - create_task_form   <!-- predicted: action_default_fallback -->
    - form{"name": "create_task_form"}
    - slot{"requested_slot": "org_id"}
    - slot{"org_id": "348"}
    - slot{"org_id": "348"}
    - slot{"requested_slot": "ws_id"}
    - slot{"ws_id": "2087"}
    - slot{"ws_id": "2087"}
    - slot{"requested_slot": "stream_id"}
    - slot{"stream_id": "1271"}
    - slot{"stream_id": "1271"}
    - slot{"requested_slot": "task_name"}
    - slot{"task_name": "bot creation"}
    - slot{"task_name": "bot creation"}
    - slot{"requested_slot": "task_priority"}
    - slot{"task_priority": "20"}
    - slot{"task_priority": "20"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm: yess
    - action_create_task   <!-- predicted: action_default_fallback -->
* goodbye: bye
    - utter_goodbye   <!-- predicted: action_default_fallback -->
    - action_restart


