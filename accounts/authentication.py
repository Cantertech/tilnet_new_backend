from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed


class SingleSessionJWTAuthentication(JWTAuthentication):
    """
    Enforces single active session per user by embedding a per-login session id (sid)
    into tokens and rejecting tokens whose sid does not match the user's current_session_id.
    """

    def get_user(self, validated_token):
        user = super().get_user(validated_token)

        try:
            token_sid = validated_token.get('sid')
        except Exception:
            token_sid = None

        # If there is no sid in the token, treat it as invalid for single-session policy
        if not token_sid:
            raise AuthenticationFailed('Invalid session. Please log in again.', code='invalid_session')

        # Ensure the user has a profile and a current_session_id set
        user_profile = getattr(user, 'userprofile', None)
        current_sid = getattr(user_profile, 'current_session_id', None) if user_profile else None

        if not current_sid or token_sid != current_sid:
            # Someone logged in elsewhere or session was rotated; this token is no longer valid
            raise AuthenticationFailed('You have been logged out because your account was used on another device.', code='session_conflict')

        return user



