from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


# def reset_user_password(request, **kwargs):
#     if request.POST:
#         current_site = Site.objects.get_current()
#         #names of the inputs in the password reset form
#         password = request.POST.get('new_password')
#         password_confirmation = request.POST.get('password_confirm')
#         #data to accept. the uid and token is obtained as keyword arguments in the url
#         payload = {
#             'uid': kwargs.get('uid'),
#             'token': kwargs.get('token'),
#             'new_password': password,
#             're_new_password': password_confirmation
#         }
#
#         djoser_password_reset_url = 'api/v1/auth/users/reset_password_confirm/'
#         protocol = 'https'
#         headers = {'content-Type': 'application/json'}
#         if bool(request) and not request.is_secure():
#             protocol = 'http'
#         url = '{0}://{1}/{2}'.format(protocol, current_site,
#                                      djoser_password_reset_url)
#         response = requests.post(url,
#                                  data=json.dumps(payload),
#                                  headers=headers)
#
#         if response.status_code == 204:
#             # Give some feedback to the user.
#             messages.success(request,
#                              'Your password has been reset successfully!')
#             return HttpResponseRedirect('/')
#         else:
#             response_object = response.json()
#             response_object_keys = response_object.keys()
#             #catch any errors
#             for key in response_object_keys:
#                 decoded_string = response_object.get(key)[0].replace("'", "\'")
#                 messages.error(request, f'{decoded_string}')
#             return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#       # if the request method is a GET request, provide the template to show. in most cases, the password reset form.
#       else:
#         return render(request, 'account/password_reset_from_key.html')



class ProfileDetailAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_view_name(self):
        return 'ProfileDetailAPIView'