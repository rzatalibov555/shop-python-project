class Uploader:

    @staticmethod
    def upload_image_to_product(instance, filename):
        return f"products/{instance.product.name}/{filename}"