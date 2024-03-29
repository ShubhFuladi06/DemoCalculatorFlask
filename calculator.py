from flask import Flask,request,render_template,jsonify
app = Flask(__name__)

@app.route("/")
def cal_page():     ### it will return render template to show the page
  return render_template('index.html')

@app.route("/math",methods=['POST'])
def calculator_ops():
   ops = request.form['operation']
   first_num = int(request.form['num1'])
   second_num = int(request.form['num2'])
   
   if (ops == 'add'):
     result = first_num + second_num
     return F"addition of {first_num} and {second_num} is {result}"
   if (ops == 'substract'):
     result = first_num - second_num
     return F"substraction of {first_num} and {second_num} is {result}"
   if (ops == 'multiply'):
     result = first_num * second_num
     return F"multiplication of {first_num} and {second_num} is {result}"
   if (ops == 'divide'):
     result = first_num / second_num
     return F"division of {first_num} and {second_num} is {result}"
   
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5002)