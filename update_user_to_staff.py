#!/usr/bin/env python
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tile_estimator.settings')
django.setup()

from accounts.models import CustomUser

# Find a user with an email and make them staff
users_with_email = CustomUser.objects.filter(email__isnull=False, email__gt='')
if users_with_email.exists():
    user = users_with_email.first()
    user.is_staff = True
    user.is_superuser = True
    user.save()
    print(f"Updated user {user.email} to staff and superuser")
    print(f"User ID: {user.id}")
    print(f"Username: {user.username}")
    print(f"Email: {user.email}")
    print(f"Is Staff: {user.is_staff}")
    print(f"Is Superuser: {user.is_superuser}")
else:
    print("No users with email found")
    # List all users
    all_users = CustomUser.objects.all()
    print("All users:")
    for u in all_users:
        print(f"- ID: {u.id}, Email: {u.email}, Username: {u.username}, Full Name: {u.full_name}")
