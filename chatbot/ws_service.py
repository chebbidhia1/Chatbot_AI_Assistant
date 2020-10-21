from graphqlclient import GraphQLClient
import json
import os
import logging

logger = logging.getLogger(__name__)

def graphql_connection(token,query,variables):
    # get environment variable for graphql host
    GRAPHQL_HOST = os.getenv('GRAPHQL_HOST')

    # create a GraphQL client instance to send requests
    client = GraphQLClient(endpoint=GRAPHQL_HOST)

    try:    
        # add the authorization tokens to the request using the client's inject_token method
        client.inject_token(token="Bearer {token}".format(token=token))

        # execute the query
        result = client.execute(query,variables)
        
        # load the result
        json_result = json.loads(result)
        return json_result
        
    except Exception as e:
        logger.debug("Unable to connect to %s.", e)


def get_organisations(token):
    """get the user's organisations
    
    Arguments:
        token (str): The user's token.

    Returns:
        List[Dict]: `buttons` the name as `title` and the id as `payload` of user's organisations.
    """
    
    query = """
    {
        meOrganizations() {
            ID,
            Name
        } 
    }
    """
    # fetch the user's organisations
    graphql_data = graphql_connection(token=token,query=query,variables=None)
    
    if not graphql_data:
        print("no result found")
        return None 

    buttons = graphql_data.get("data").get("meOrganizations")
    if not buttons:
        print("no org found")
        return None

    for button in buttons:
        # changing keys of dictionary 
        button['title'] = button.pop('Name')  
        button['payload'] = button.pop('ID') 

    print(buttons)        
    return buttons

def get_workspaces(token,org_id):
    """get the user's workspaces
    
    Arguments:
        token (str): The user's token.
        org_id (str): The organisation id.

    Returns:
        List[Dict]: `workspaces` the name as `title` and the id as `payload` of the user's workspaces.
        Dict[Text, List[Dict]]: `streams` the key as `ws_id` and the stream_list as the user's streams.
    """
    
    query = """
    {
        meWorkspacesByOrganization(organizationID : "%s") {
            workspaces{
                id,
                name,
                streams{
                    streams{
                    id,
                    name
                    }
                }
            }
        }
    }
    """ % (org_id)
    
    # fetch the user's workspaces
    graphql_data = graphql_connection(token=token,query=query,variables=None)
    if not graphql_data:
        print("no result found")
        return None

    data = graphql_data.get("data")    
    if not data:
        print("no ws found")
        return None

    # get workspace list
    ws_list = data.get("meWorkspacesByOrganization").get("workspaces")

    streams = {} 
    workspaces= []

    for ws in ws_list:
        stream_list = []
        # get the ws id
        ws_id = ws.get('id')
        # get the ws name
        ws_name = ws.get('name')
        # append the title and the payload to workspaces list
        workspaces.append({
            "title" : ws_name ,
            "payload" : ws_id
        })
        
        for stream in ws.get("streams").get("streams"):
            # append the title and the payload to stream_list
            stream_list.append({
                "title" : stream.get('name') ,
                "payload" : stream.get('id') 
            })
        # update streams dict with stream list
        streams.update({
            ws_id : stream_list
        })

    print("workspaces",workspaces)
    print("streams",streams)

    return workspaces, streams  

def get_workspacesByName(token,org_id):
    """get the user's workspaces
    
    Arguments:
        token (str): The user's token.
        org_id (str): The organisation id.

    Returns:
        List[Dict]: `workspaces` the name as `title` and the id as `payload` of the user's workspaces.
        Dict[Text, List[Dict]]: `streams` the key as `ws_id` and the stream_list as the user's streams.
    """
    
    query = """
    {
        meWorkspacesByOrganization(organizationID : "%s") {
            workspaces{
                id,
                name,
                streams{
                    streams{
                    id,
                    name
                    }
                }
            }
        }
    }
    """ % (org_id)
    
    # fetch the user's workspaces
    graphql_data = graphql_connection(token=token,query=query,variables=None)
    if not graphql_data:
        print("no result found")
        return None

    data = graphql_data.get("data")    
    if not data:
        print("no ws found")
        return None

    # get workspace list
    ws_list = data.get("meWorkspacesByOrganization").get("workspaces")

    
    workspaces= []

    for ws in ws_list:
        ws_name = ws.get('name')
        workspaces.append(ws_name)

    print("workspaces",workspaces)
    

    return workspaces 

def create_task(token,name,stream_id,priority):
    """create the task
    
    Arguments:
        token (str): The user's token.
        name (str): The task name.
        stream_id (int): The task stream.
        priority (int): The task priority.

    Returns:
        Dict: `task` the name and id of the created task.
    """
    
    query = """
        mutation addTask($name: String!, $streamID: ID!, $priority: Int) {
            createNewTask(input: {streamID: $streamID, name: $name, priority: $priority}) {
                id
                name
            }
        }
    """
    variables = {
        "name": name,
        "streamID": stream_id,
        "priority": priority
    }

    # create the task
    graphql_data = graphql_connection(token=token,query=query,variables=variables)
    
    if not graphql_data:
        print("no result found")
        return None

    # fetch the created task
    task = graphql_data.get("data").get("createNewTask") 

    if not task:
        print("the task was not created")
        return None
            
    return task

def create_stream(token,name,wsID):
    query = """
        mutation createStream($name: String!, $wsID: ID!) {
            createNewStream(input: {wsID: $wsID, name: $name}) {
                id
                name
            }
        }
    """
    variables = {"name": name,
                "wsID" : wsID
                }

    graphql_data = graphql_connection(token=token,query=query,variables=variables)
    
    if not graphql_data:
        print("no result found")
        return None

    # fetch the created stream
    stream = graphql_data.get("data").get("createNewStream") 

    if not stream:
        print("the stream was not created")
        return None
            
    return stream

def create_workspace(token,name,typ,description,organizationID):
    query = """
        mutation CreateWorkspaceWithTemplateInput($organizationID: String!,$name: String!, $typ: String!, $description: String!) {
            createWorkspaceWithTemplate(input: {name : $name , typ:$typ ,  description : $description ,organizationID: $organizationID }) {
                id
                name
            }
        }
    """
    variables = {
	    "name": name ,
	    "typ":  typ ,
	    "description": description ,
        "organizationID": organizationID
                }

    graphql_data = graphql_connection(token=token,query=query,variables=variables)
    
    if not graphql_data:
        print("no result found")
        return None

    # fetch the created stream
    workspace = graphql_data.get("data").get("createWorkspaceWithTemplate") 

    if not workspace:
        print("the workspace was not created")
        return None
            
    return workspace

if __name__ == "__main__":
    token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjM0ZjcxYTRlOTU0NTk0ZjYwM2UzOTZiN2UyNWRlNTliOTNlNjMyYjYifQ.eyJpc3MiOiJodHRwczovL3Nzby5kZXYubWVlcmFzcGFjZS5jb20iLCJzdWIiOiJDaVF3TkRRMk56ZGlOUzAyTjJaaUxUUTFOVGt0T0dNNVpDMWtPR1ZqWVRVM1lqQXhNREVTQld4dlkyRnMiLCJhdWQiOiJ3b3Jrc3BhY2UiLCJleHAiOjE1OTgwODYyMzMsImlhdCI6MTU5NzgyNzAzMywiYXRfaGFzaCI6ImprQlQyM3hJY1c2ZFp6RElZcEpNQVEiLCJlbWFpbCI6Imphc3Nlci5iZW5hYmRhbGxhaEB0YXJnZXQtZW5lcmd5c29sdXRpb25zLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYW1lIjoiSmFzc2VyIn0.hdWzJH2eQ4ib_fteTDBHAGp8sybuZ3YpVeoOcnlGVEbfwyPCoo82pn1GsPvv5AzHv7e2oJvKXzbocfiphV-xipuuc70DSZuKa_SSl_XyuZqTVg6MBUEqap1VDowvyBVLtqSXh6DNW3lumafE_KHbAzeHQRbva9Vk2tIomhIFWEvP1HKu0-k-EqYxkskdkhPIzuzQ9zO3YVLTDZGu-WeQxaTymq58RniW5JosfxLoehsiZO-_TSd4j4lhMdsn1bU3nlYXfaUTa_fSiXzpUW-cgIljR2XdKmAJhe8p16WyNPgYMBw179W3ek6Gvnwt5WLQ1eKGmuFmacqDGMvbhrwBng"
    #create_task(token,"chat&",1312, 30)
    print("**********")
    #org_list = get_organisations(token =token) 
    #workspaces = get_workspaces(token =token,org_id="625")
    #create_stream(token,"from terminal",1357)
    #create_workspace(token,"from_term","General Workspace","new_test","548")
    get_workspacesByName(token,548)