from schema.aws.ecr.ecrimageaction import Marshaller
from schema.aws.ecr.ecrimageaction import AWSEvent
from schema.aws.ecr.ecrimageaction import ECRImageAction


def lambda_handler(event, context):
    """Sample Lambda function reacting to EventBridge events

    Parameters
    ----------
    event: dict, required
        Event Bridge Events Format

        Event doc: https://docs.aws.amazon.com/eventbridge/latest/userguide/event-types.html

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
        The same input event file
    """

    #Deserialize event into strongly typed object
    awsEvent:AWSEvent = Marshaller.unmarshall(event, AWSEvent)
    detail:ECRImageAction = awsEvent.detail

    #Execute business logic

    #Make updates to event payload, if desired
    awsEvent.detail_type = "HelloWorldFunction updated event of Something";

    #Return event for further processing
    return Marshaller.marshall(awsEvent)
