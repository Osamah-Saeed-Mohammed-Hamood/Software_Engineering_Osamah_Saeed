from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator,FileExtensionValidator
import magic


f_name_validetor = RegexValidator(
    regex=r'^[A-Z][a-zA-Z]*$',
    message="❌ الاسم الاول يجب ان يبدأ بحرف Capital و يحتوي على أحرف فقط"
)

ext_validator = FileExtensionValidator(['png','jpg','jpeg'])

def validate_image_mimetype(file):
    accept = ['image/png', 'image/jpg', 'image/jpeg']
    file_mime_type = magic.from_buffer(file.read(1024), mime=True)
    if file_mime_type not in accept:
        raise ValidationError("❌ الصورة غير مدعومة")