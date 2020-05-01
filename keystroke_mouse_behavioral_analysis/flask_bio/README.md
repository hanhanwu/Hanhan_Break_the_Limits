# Flask Bio

## How to use Flask

### Install Flask
* Better to use virtual env
  * `source activate venv`
  * `conda deactivate`
* `pip install Flask`

### Setup
* Make sure there is no other app is using localhost.
* The .html page must be saved under "templates/" folder.
  * form action="http://localhost:5000/"
* Write a python file similar to [flask_bio_behavior.py][1]
  * Just need `app.run(debug=True)` at the bottom. I didn't really need any other command
* If you got code 200, you can go to "http://localhost:5000/"


### References
* [A Flask project example - twitter hate speech classification][2]


[1]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/keystroke_mouse_behavioral_analysis/flask_bio/flask_bio_behavior.py
[2]:https://www.analyticsvidhya.com/blog/2020/04/how-to-deploy-machine-learning-model-flask/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29
