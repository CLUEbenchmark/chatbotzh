## greet
* greet
  - utter_greet

## general disease 
* disease
  - action_report_general_disease
  - utter_report_disease

## simple path
* disease_address{"address": "上海"}
  - action_report_disease
  - utter_report_disease

## bad mood
* mood_unhappy
  - utter_help_heppier

## greet > Disease > address path
* greet
  - utter_greet
* disease_address{"address": "上海"}
  - action_report_disease
  - utter_report_disease

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_bot_challenge

## ask advice
* advice
  - utter_advice
