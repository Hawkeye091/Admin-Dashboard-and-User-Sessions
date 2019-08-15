# Admin-Dashboard-and-User-Sessions

## Requirements 

pip install django-admin

## A look at Admin Dashboard

1.Create a super user by using the command :
python manage.py createsuperuser and login as admin on http://127.0.0.1:8000/admin/ :

![Screenshot (30)](https://user-images.githubusercontent.com/25239737/63088556-f17a1e80-bf72-11e9-967e-001b7694a0ba.png)

2.On clicking on MySimple Model you can view the contents of the table :

![Screenshot (31)](https://user-images.githubusercontent.com/25239737/63088578-03f45800-bf73-11e9-979c-99090de4e4c1.png)

3.Search bar available to filter on basis of Employee Id and name :

![Screenshot (32)](https://user-images.githubusercontent.com/25239737/63088598-0e165680-bf73-11e9-8476-44f878fa1369.png)

4.You can download the contents in the form of a CSV file by selecting the action download to CSV on the dropdown :

![Screenshot (33)](https://user-images.githubusercontent.com/25239737/63088613-18385500-bf73-11e9-88a9-0df91da23cce.png)

## A look at the base page for Users

1.You can visit the base page http://127.0.0.1:8000/ :

![Screenshot (34)](https://user-images.githubusercontent.com/25239737/63088693-4ae24d80-bf73-11e9-9c88-68c14a1a98cc.png)

2.Click onto register to add new users :

![Screenshot (35)](https://user-images.githubusercontent.com/25239737/63088713-59c90000-bf73-11e9-8656-8c4f9cc8070a.png)

3.The registered users can login :


![Screenshot (38)](https://user-images.githubusercontent.com/25239737/63089916-29836080-bf77-11e9-9c97-5dbd83c4813c.png)

4.And logout as well :


![Screenshot (37)_LI](https://user-images.githubusercontent.com/25239737/63089410-60587700-bf75-11e9-9928-bc582d25572f.jpg)

5.The session expires automatically on 5 minutes of inactivity.
