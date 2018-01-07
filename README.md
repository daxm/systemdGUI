Welcome to the **systemd GUI** project!

I've seen a lot of projects like this and I have no illusions that I'm going to do something better/cooler than what has
already been done.  That said, I'm going to built this project anyway as a means of improving my Python skills and 
systemd/journal knowledge.

I eagerly would like any help/adivce people might have regarding this goal.  I'm also willing to work with someone to 
improve this project's code/functionality.

Okay, enough with the ramble.  This project is a Flask application that runs on port 7890.  To run this project issue
the command
```bash
python3 app.py
```
Then open up a browser and access **http://<ip of system>:7890**.

TODOs:
- Add Logging
- Integrate "os commands" to gather systemctl and/or journalctl outputs.