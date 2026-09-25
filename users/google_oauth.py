from rest_framework.generics import CreateAPIView
from serializer import GoogleSerializer
from users.models import CustomUser

class GoogleOAuthApiView(CreateAPIView):
    serializer_class = GoogleSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)

        code = serializer.validated_data('code')
        token_response = request.post(
            url="https://oauth2.googleapis.com/token",
            data={
                "code":code,
                "client_id":"",
                "cliet_secret":"",
                "redirect_url":"",
                "grand_type":"authorization_code"
            }
        )

        token_data = token_response.json()
        access_token = token_data.get('access_token')
        user_info =request.get(
            url = "https://",
            params = {"alt":"json"},
            header={"Authorization":f"Bearer {access_token}"},
        ).json()

        print('USER INFO', user_info)
        email = user_info["email"]

        user ,created = CustomUser.objects.get_or_create(email=email)
        refresh = RefreshToken.for_user(user)
        refresh['email']