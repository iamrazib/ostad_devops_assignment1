# ostad_devops_assignment1
Local DevOps Demo Application and Exposing Local Application through ngrok


**Task 1: Local DevOps Demo Application**

**Technology Used:** Python, Flask, Visual Studio Code.

**Implementation:** I created a simple Python web application using Flask in Visual Studio Code. I installed the required dependency and ran the application using the `python appmain.py` command.

**Verification:** The application was accessed through `http://127.0.0.1:5000`. The browser displayed the application page, and the `/status` endpoint returned the running status.

-------------------------------------------

### Task 2: Exposing Local Application Using ngrok

**Tools Used:** Python, Flask, VS Code, and ngrok.

**Implementation:** I successfully exposed my locally running Flask application to the internet using ngrok. I configured ngrok authentication and executed the `ngrok http 5000` command to establish a secure public tunnel.

**Public URL:** (https://corporate-evacuate-flashy.ngrok-free.dev/)

**Verification:** I opened the generated public URL in a web browser and confirmed that my Flask application was accessible through the internet.

**Real-World Use Case:** ngrok allows developers to share locally running applications with remote team members or clients without deploying them to a production server. It is also useful for testing webhooks and external API integrations.

**Conclusion:** This task helped me understand how to make a local application publicly accessible using a secure tunnel.