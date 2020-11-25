# from src.Sleeper import sleeper
#
# # import kivy module
# import kivy
#
# # base Class of your App inherits from the App class.
# # app:always refers to the instance of your application
# from kivy.app import App
#
# # this restrict the kivy version i.e
# # below this kivy version you cannot
# # use the app or software
# kivy.require('1.9.1')
#
# # creates the button in kivy
# # if not imported shows the error
# from kivy.uix.button import Button
#
# # The TextInput widget provides a
# # box for editable plain text
# from kivy.uix.textinput import TextInput
#
# # BoxLayout arranges widgets in either
# # in vertical fashion that
# # is one on top of another or in
# # horizontal fashion that is one after another.
# from kivy.uix.boxlayout import BoxLayout
#
# # to change the kivy default settings we use this module config
# from kivy.config import Config
#
# # 0 being off 1 being on as in true / false
# # you can use 0 or 1 && True or False
# Config.set('graphics', 'resizable', True)
#
# # Create the App class
# class SleepyGui(App):
#
#     def __init__(self):
#       App.__init__(self)
#       self.text_input: TextInput = None
#       self.button: Button = None
#       self.layout: BoxLayout = None
#
#     # defining build()
#     def build(self):
#
#                 # Telling orientation
#         self.layout = BoxLayout(orientation ='vertical', )
#
#         # Adding the text input
#         self.text_input = TextInput(font_size = 30,
#                     size_hint_y = None,
#                     height = 100)
#
#         # Adding Button and styling
#         self.button = Button(text ="Sleepy timer :)",
#                    font_size ="20sp",
#                    background_color =(.67, 1, .33, 1),
#                    color =(1, 1, 1, 1) )
#         self.button.bind(on_press=self.execute_timer)
#
#         self.layout.add_widget(self.text_input)
#         self.layout.add_widget(self.button)
#
#         return self.layout
#
#     def execute_timer(self, instance):
#       print(instance)
#       if self.text_input.text == '':
#         self.button.text = 'Please provide a number (in minutes)'
#       elif not str(self.text_input.text).isnumeric():
#         self.button.text = 'Please provide a number a valid number (in minutes)'
#       else:
#         self.button.text = 'Sleeping...'
#         sleeper(int(self.text_input.text))
