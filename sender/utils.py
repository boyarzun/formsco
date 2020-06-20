import re
import bleach
import requests


def get_form_content(data):
    content = ""
    for key in data:
        if key != "g-recaptcha-response":
            label = key
            label = " ".join(re.split("[^a-zA-Z]", label))
            label = " ".join(re.split("(?=[A-Z])", label))
            label = label[1:] if label[0] == " " else label
            label = label.title()

            form_data = bleach.clean(data.get(key), tags=[])
            content += "<strong>" + label + "</strong>" + ": " + form_data + "<br/>"

    return content


def get_current_host(request) -> str:
    scheme = "https" if request.is_secure() else "http"
    return f"{scheme}://{request.get_host()}"


def re_captcha(request, secret_key):
    """ Begin reCAPTCHA validation """

    if secret_key == None:
        return True

    recaptcha_response = request.POST.get("g-recaptcha-response")

    data = {"secret": secret_key, "response": recaptcha_response}

    r = requests.post("https://www.google.com/recaptcha/api/siteverify", data=data)
    result = r.json()

    """ End reCAPTCHA validation """

    if result["success"]:
        return True
    else:
        return False


def get_emails(string: str):
    """ Get emails from string """
    # 'one@example.com, two@example.com' to
    # ['one@example.com', 'two@example.com']

    emails = list(string.replace(" ", "").split(","))
    return emails if len(emails) > 1 else emails[0]

