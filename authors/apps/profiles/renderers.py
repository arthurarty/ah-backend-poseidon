import json

from rest_framework.renderers import JSONRenderer


class ProfileJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        # If the view throws an error (such as the user can't be authenticated
        # or something similar), `data` will contain an `errors` key. We want
        # the default JSONRenderer to handle rendering errors, so we need to
        # check for this case.
        response = json.dumps({'profile': data})

        if isinstance(data, list):
            return json.dumps({'profiles': data})

        errors = data.get('errors', None)

        if errors is not None:
            # As mentioned about, we will let the default JSONRenderer handle
            # rendering errors.
            response = super(ProfileJSONRenderer, self).render(data)

        # Finally, we can render our data under the "profile" namespace.
        return response


class NotificationJSONRenderer(JSONRenderer):
    """
    Override default renderer to customise output
    """
    charset = 'utf-8'

    def render(self,
               data,
               accepted_media_type='application/json',
               renderer_context=None):
        if isinstance(data, list):
            errors = None
        else:
            errors = data.get('errors', None)

        if errors is not None:
            return super(NotificationJSONRenderer, self).render(data)

        return json.dumps({'notifications': data})
