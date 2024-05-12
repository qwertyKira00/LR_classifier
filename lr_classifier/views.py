import json
from json import JSONDecodeError

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .predict import predict
from .output import convert_predictions_to_output


@csrf_exempt
def input_view(request):
    if request.method == 'POST':
        body = request.body
        body = body.decode('utf-8')
        try:
            body = json.loads(body)
        except JSONDecodeError:
            return JsonResponse({'Ошибка': 'Неверное тело запроса'}, status=400)

        legal_rule_text = body.get('texts', '')
        if legal_rule_text:
            moral_predictions, type_predictions = predict([legal_rule_text])
            return JsonResponse(
                convert_predictions_to_output(
                    legal_rule_text,
                    moral_predictions,
                    type_predictions,
                )
            )
        else:
            return JsonResponse({'Ошибка': 'Отсутствует НПА на входе'}, status=400)
    else:
        return JsonResponse()
