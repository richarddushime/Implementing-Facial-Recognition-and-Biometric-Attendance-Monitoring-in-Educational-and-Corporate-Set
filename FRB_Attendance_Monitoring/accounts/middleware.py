from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages

class AccountCheckMiddleware(MiddlewareMixin):
    ADMIN_USER_TYPE = '1'
    STUDENT_USER_TYPE = '2'

    ALLOWED_ADMIN_MODULES = ['students.views']
    ALLOWED_STUDENT_MODULES = ['staff.views']
    AUTHENTICATION_MODULES = ['django.contrib.auth.views']

    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        user = request.user

        if user.is_authenticated:
            if user.user_type == self.ADMIN_USER_TYPE:
                if modulename not in self.ALLOWED_ADMIN_MODULES and request.path != reverse('fetch_ballot'):
                    messages.error(request, "You do not have access to this resource")
                    return redirect(reverse('adminDashboard'))

            elif user.user_type == self.STUDENT_USER_TYPE:
                if modulename not in self.ALLOWED_STUDENT_MODULES:
                    messages.error(request, "You do not have access to this resource")
                    return redirect(reverse('voterDashboard'))

            else:
                # No user type mentioned? Redirect to login.
                return redirect(reverse('account_login'))

        else:
            # If the path is related to authentication, pass
            if request.path in [reverse('account_login'), reverse('account_register')] or modulename in self.AUTHENTICATION_MODULES:
                pass

            elif modulename in self.ALLOWED_ADMIN_MODULES or modulename in self.ALLOWED_STUDENT_MODULES:
                # If a visitor tries to access administrator or voters functions without being logged in
                messages.error(request, "You need to be logged in to perform this operation")
                return redirect(reverse('account_login'))

            else:
                return redirect(reverse('account_login'))
