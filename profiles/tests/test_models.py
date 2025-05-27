from django.test import TestCase
from profiles.models import UserProfile, Follow
from django.contrib.auth.models import User

class UserProfileModelTest(TestCase):
    
    def setUp(self):
        self.user1 = User.objects.create_user(username="user1", password="1234")
        self.user2 = User.objects.create_user(username="user2", password="1234")
        self.profile1 = UserProfile.objects.create(user=self.user1, bio="hola", birth_date="2000-01-01")
        self.profile2 = UserProfile.objects.create(user=self.user2, bio="chau", birth_date="2000-02-02")
        
    def test_follow_user(self):
        self.profile1.follow(self.profile2)
        
        self.assertTrue(Follow.objects.filter(follower=self.profile1, following=self.profile2).exists())
        
    def test_unfollow_user(self):
        self.profile1.follow(self.profile2)
        self.assertTrue(Follow.objects.filter(follower=self.profile1, following=self.profile2).exists())
        self.profile1.unfollow(self.profile2)
        self.assertFalse(Follow.objects.filter(follower=self.profile1, following=self.profile2).exists())

        
class FollowModelTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="user1", password="1234")
        self.user2 = User.objects.create_user(username="user2", password="1234")
        self.profile1 = UserProfile.objects.create(user=self.user1, bio="hola", birth_date="2000-01-01")
        self.profile2 = UserProfile.objects.create(user=self.user2, bio="chau", birth_date="2000-02-02")
        
    def test_unique_follow_once_time(self):
        Follow.objects.create(follower=self.profile1, following=self.profile2)
        self.assertEqual(Follow.objects.filter(follower=self.profile1, following=self.profile2).count(), 1)
        Follow.objects.get_or_create(follower=self.profile1, following=self.profile2)
        self.assertEqual(Follow.objects.filter(follower=self.profile1, following=self.profile2).count(), 1)