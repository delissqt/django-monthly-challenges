What are "Views"?

Te logic that is executed for differents URLs (and Http methods)

|Function|Class|

Code that handles (evaluates) requests and returns responses

* Load & prepare data
* Run any other business logic
* Prepare and return response data (e.g. HTML)
  



  Views are responsible for processing request (parsing the URL, Http method ans potential request data)
  and **creating a response**



 make reference to parameter un Url Path -1rs month
make refernece to variable in for - 2sc month
challenges/templates/challenges/index.html
{% url "month-challenge" month=month %}