#import torch

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
#from transformers import BertTokenizer, BertForQuestionAnswering

from .serializers import UserSerializer, AnswerQuestionSerializer

class UserAPI(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class AnswerQuestionAPI(APIView):
    def post(self, request):
        serializer = AnswerQuestionSerializer(data = request.data)
        if serializer.is_valid():
            answer_question = Prueba.funcion(data = request.data.get('answer_text'))
            serializer.save()
            return Response([answer_question], status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class AnswerTextAPI(APIView):
    """ Relacionado con la gestión del texto donde se encuentra la respuesta """
    def post(self, request):
        pass

class QuestionAPI(APIView):
    """ Relacionado con la gestión de la preguntas """
    def post(self, request):
        pass

class Prueba:
    @staticmethod
    def funcion (data):
        return data

""" class Bert:
    model = BertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
    tokenizer = BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
    @staticmethod
    def answer_question(answer_text, question):
        # ======== Tokenize ========
        # Aplicamos el tokenizer al texto de entrada, tratándolos como un par de texto.
        input_ids = tokenizer.encode(question, answer_text)

        # Informa el largo de la secuencia de entrada.
        long_imput_sequence = len(input_ids)

        # ======== Set Segment IDs ========
        # Busque en input_ids la primera instancia del token '[SEP]'.
        sep_index = input_ids.index(tokenizer.sep_token_id)

        # El número de tokens del segmento A incluye la [SEP] token istelf.
        num_seg_a = sep_index + 1

        # El resto son segmento B.
        num_seg_b = len(input_ids) - num_seg_a

        # Construye la lista de 0s y 1s.
        segment_ids = [0]*num_seg_a + [1]*num_seg_b

        # Debe haber un ID de segmento para cada token de entrada.
        assert len(segment_ids) == len(input_ids)

        # ======== Evaluate ========
        # Ejecute nuestra pregunta a través del modelo.
        start_scores, end_scores = model(torch.tensor([input_ids]), # Los tokens que representan nuestro texto de entrada.
                                            token_type_ids=torch.tensor([segment_ids])) # Los ID de segmento para diferenciar la pregunta del texto de respuesta

        # ======== Reconstruct Answer ========
        # Encuentra las fichas con las puntuaciones más altas de `start` y` end`.
        answer_start = torch.argmax(start_scores)
        answer_end = torch.argmax(end_scores)

        # Obtenga las versiones de cadena de los tokens de entrada.
        tokens = tokenizer.convert_ids_to_tokens(input_ids)

        # Comience con el primer token.
        answer = tokens[answer_start]

        # Seleccione los tokens de respuesta restantes y únalos con espacios en blanco.
        for i in range(answer_start + 1, answer_end + 1):

            # Si se trata de un token de subpalabras, recombínelo con el token anterior.
            if tokens[i][0:2] == '##':
                answer += tokens[i][2:]
            # De lo contrario, agregue un espacio y luego el token.
            else:
                answer += ' ' + tokens[i]
        return (long_imput_sequence, answer)
    """     
  