# SimpleWeatherApp
#### Video Demo: https://youtu.be/_h9l0IBLtwg
#### Description:
"Implementing a simple weather application using Tkinter and Python"

**PRESENTATION**

Hello everyone, my name is Marouane. For my CS50 course final project, I contemplated various project ideas. However, considering the time constraints and the need to acquire new skills, I opted for a simpler project. I decided to create a weather desktop app that displays temperature and other relevant weather information. After some research, I found that Python would be well-suited for the task, especially with its GUI library, Tkinter.
I embarked on learning about tkinter and how to fetch weather data to integrate it seamlessly into my app. The goal is to provide a user-friendly interface that not only showcases my understanding of Python and Tkinter but also delivers practical value by presenting accurate and up-to-date weather information. I'm excited about this project and look forward to sharing the final product with you all.

**LIBRARY&APIs**

In the process of building this app, I realized that I would need to leverage various Python libraries to enhance its functionality. One such library is PIL (Python Imaging Library), which plays a crucial role in image manipulation. I'll be using it to open and manipulate images of cities that the API returns as part of the weather information.
Furthermore, the API responses come in the form of JSON objects, which was a new concept for me to delve into. Learning about RESTful APIs became an integral part of the project, as it's the industry standard for handling communication between different systems. This exploration allowed me to understand how to efficiently retrieve and parse data from the API to seamlessly integrate it into my weather app. It's been a valuable learning experience, and I'm eager to see the culmination of these efforts in the final product.

**SCREENSHOTS**

![demo from the app](screenshots/doha.png "screenshot")

![demo from the app](screenshots/dubai.png "screenshot")

![demo from the app](screenshots/madrid.png "screenshot")

![demo from the app](screenshots/moscow.png "screenshot")

**ERROR HANDLING**

To handle cases where some of the APIs return nothing, I've implemented a try-except block to manage potential errors gracefully. This allows the application to handle exceptions without crashing and provides a more user-friendly experience. By incorporating this error-handling mechanism, I aim to ensure the robustness of the app and enhance its overall reliability. If some specific errors or scenarios need to be addressed, I can tailor the try-except block accordingly. This approach contributes to a smoother user experience and reinforces the resilience of the weather app under various conditions.

