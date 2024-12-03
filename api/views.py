from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from PIL import Image
from io import BytesIO

class ImageProcessingView(APIView):
    def post(self, request):
        # 요청 데이터에서 파일 가져오기
        file = request.FILES.get('multipartFile')

        if not file:
            return Response({"error": "No file provided."}, status=status.HTTP_400_BAD_REQUEST)
        
        if not file.name.endswith('.png'):
            return Response({"error": "Only .png files are supported."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # 받아온 이미지를 Model에 Feed해서 결과 산출
            # TODO
            
            image = Image.open(file)
            suspiciousness = 0.9

            # 응답 반환
            return Response({"suspiciousness": suspiciousness}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": f"Failed to process the image: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
