import facebook

token = 'EAACEdEose0cBAEHgVD37ZB20ao9BvfC3iyvjtpb7hZBjltF4CtD8MbYfUj0hkDOa6Uvjxz0jZAd8U7ZBNUD3PSAS4StDrr3P27KJSb9r1UKRKnGI6PzfZBWZBC0BggmnZBLsS7jqeXAtBmsMlT7ZB3ZBi3Q1IVfdHMcyBm9VHb6zOZCQZDZD'

graph = facebook.GraphAPI(token)
profile = graph.get_object('me')
friends = graph.get_connections("me", "friends")
connect = graph.get_connections('me', '')

print connect

gender = profile['gender']
print gender

age = profile['first_name']
print age

friend_list = [friend['name'] for friend in friends['data']]

print friend_list
