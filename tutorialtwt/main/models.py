from django.db import models

# Create your models here.
class ToDoList(models.Model):
    #whenever we create a new attribute of our model we create it as a class variable.  We name the attribute and then we do the type of field we want stored
    name = models.CharField(max_length=200) #CharField is a type of field that we can store information in

    #for if we want to print out something meaningful
    def __str__(self):
        return self.name

class Item(models.Model):
    #Item is a little different because it's a part of the to-do list
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE) #ToDoList isn't defined in django, so we create a ForeignKey, in this case a ToDoList object.  on_delete is just saying if we delete ToDoList we'll have to delete it all and CASCADE should do that
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text