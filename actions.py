# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message("Hello World!")
#
#         return []

from typing import Any, Text, Dict, List

from rasa_sdk import Tracker, Action
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

from service.wuhan import get_detail_info

class ActionReportDisease(Action):
    def __init__(self):
       pass 

    def name(self) -> Text:
        return "action_report_disease"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        address = tracker.get_slot('address').replace('市', '')
        address = address.replace('省', '')
        if not address:
          disease_data = get_detail_info('general')
          return [SlotSet("matches", "{}。如果想了解具体信息，请输入具体地址".format(disease_data))]

        try:
            disease_data = get_detail_info(address)
        except Exception as e:
            disease_data = str(e) + ' and your input is run. pls input 地点。例如北京今天的情况'

        return [SlotSet("matches", "{}".format(disease_data))]


class ActionGeneralReportDisease(Action):
    def __init__(self):
       pass 

    def name(self) -> Text:
        return "action_report_general_disease"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        disease_data = get_detail_info('general')
       # 
       # try:
       #     disease_data = get_detail_info()
       # except Exception as e:
       #     disease_data = str(e) + ' and your input is run. pls input 地点。例如北京今天的情况'

        return [SlotSet("matches", "{}".format(disease_data))]

