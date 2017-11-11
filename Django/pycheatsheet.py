# 1. django-admin startproject (project name)
# 2. create apps folder
# 3. add __init__.py in apps folder
# 4. python ../manage.py startapp (app name)
# 5. add urls.py file and connect to project url page
# 6. create views and import libraries
# 7. create templates adn static folders


# make migrations
# migrate
# shell

# Creating a new record
Blog.objects.create({{field1}}="{{value}}", {{field2}}="{{value}}", etc) # creates a new record in the Blog table
Blog.objects.create(name="Star Wars Blog", desc="Everything about Star Wars") # creates a new blog record
Blog.objects.create(name="CodingDojo Blog") # creates a new blog record with the empty desc field

# Alternative way of creating a record
b = Blog(name="Disney Blog", desc="Disney stuff")
b.name = "Disney Blog!"
b.desc = "Disney stuff!!!"
b.save()

# Basic Retrieval
Blog.objects.first() - retrieves the first record in the Blog table
Blog.objects.last() - retrieves the last record in the Blog table
Blog.objects.all() - retrieves all records in the Blog table
Blog.objects.count() - shows how many records are in the Blog table

# Updating the record - once you obtain an object that has the record you want to modify, use save() to update the record.  For example
b = Blog.objects.first() # gets the first record in the blogs table
b.name = "CodingDojo Blog"  # set name to be "CodingDojo Blog"
b.save() # updates the blog record

# Deleting the record - use delete().  For example
b = Blog.objects.get(id=1)
b.delete() # deletes that particular record

# Other methods to retrieve records
Blog.objects.get(id=1) #- retrieves where id is 1; get only retrieves 1 record
Blog.object.filter(name="mike") #- retrieves records where name is "mike"; returns multiple records
Blog.objects.exclude(name="mike") #- opposite of filter; returns multiple records
Blog.objects.order_by("created_at") #- orders by created_date field
Blog.objects.order_by("-created_at") #- reverses the order
Blog.objects.raw("SELECT * FROM {{app_name}}_{{class/table name}}") #- performs a raw SQL query
Blog.objects.first().comments.all() #- grabs all comments from the first Blog
Blog.objects.get(id=15).comments.first() #- grabs the first comment from Blog id = 15
Comment.objects.get(id=15).blog.name #- returns the name of the blog where Comment id = 15 belongs to

# Setting Relationship
Comment.objects.create(blog=Blog.objects.get(id=1), comment="test") - create a new comment where the comment's blog points to Blog.objects.get(id=1).

# Conditions
You can do a more complicated search than just if a given field is equal to a given value. Instead of just passing in the field name as a keyword argument to .get, .filter, or .exclude, you'd pass the field name__lookup type (that's a double underscore, also known as a "dunder" for people on-the-go). 

# For example:
Admin.objects.filter(first_name__startswith="S") - filters objects with first_name that starts with "S"
Admin.objects.exclude(first_name__contains="E") - excludes objects where first_name contains "E"
Admin.objects.filter(age__gt=80)  - filters objects with age greater than 80

# objects.create(="") is for creating objects
Dojo.objects.create(city="New York City", state="NY")

# objects.get(="") is for getting single entires
User.objects.get(id=1)
User.objects.get(first_name="mike")

# objects.filter(="") is for getting multiple entries
Dojo.objects.filter(city="New York City")
User.objects.filter(first_name__startswith="m")

# objects.exclude(="") is for getting everything but something
User.objects.exlcude(last_name="Thomas")

# __condition filter is for adding to an instance
User.objects.filter(first_name__startswith="M")
Dojo.objects.exclude(city__contains="New")

# combine queries with a . like below:
User.objects.filter(last_name__contains="o").exclude(first_name__contains="i")

# displaying in the template:

def index(request):
	users = User.objects.filter(age__lt=70)|User.objects.filter(first_name__startswith="S")
	context = {"users": users}
	return render(request, "users/index.html", context)

## iterating through the data in django templating language


# Validating Information:
# - Take post request and route it to models. Model will do validation. Make sure info is correct. All of that should be in the model. It's much safer
# - We add a "manager".


# Look back on Dojo Ninjas, Belt Reviewer, Courses, and Login_Reg assignments for most help on copypasta and reference