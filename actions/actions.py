# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

# --------------------------------------------------------------------------------

# actions/actions.py
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionSubmitReservation(Action):

    def name(self) -> Text:
        return "action_submit_reservation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        guests = tracker.get_slot('guests')
        names = tracker.get_slot('names')
        dates = tracker.get_slot('dates')
        email = tracker.get_slot('email')
        requests = tracker.get_slot('requests')

        if requests:
            response = (f"Reservation for {guests} guests from {dates} has been submitted "
                        f"with the email {email}. Special requests: {requests}. We will contact you shortly. "
                        f"Please check your mails!")
        else:
            response = (f"Reservation for {guests} guests from {dates} has been submitted "
                        f"with the email {email}. We will contact you shortly. Please check your mails!")

        dispatcher.utter_message(text=response)

        return []
