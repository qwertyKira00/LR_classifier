from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .predict import predict
from .output import convert_predictions_to_output


@csrf_exempt
def input_view(request):
    if request.method == 'POST':
        legal_rule_text = request.POST.get('legal_rule_text', '')
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
