from furryFunniesApp.authors.models import Author


def get_profile():
    profile = Author.objects.first()

    return profile
