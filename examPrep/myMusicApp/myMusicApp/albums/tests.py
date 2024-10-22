from django.test import TestCase

from myMusicApp.profiles.models import Profile

# Create your tests here.
profile = Profile.objects.get(id=7)  # Replace with the correct ID
profile.album_set.all().count()  # Should return 3 (if 3 albums are associated)
profile.delete()  # This should delete both the profile and its albums
