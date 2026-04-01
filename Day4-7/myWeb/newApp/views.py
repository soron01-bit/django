from django.shortcuts import render
from .models import product
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
import os
from concurrent.futures import ThreadPoolExecutor, as_completed


def optimize_product_image(product_instance):
    """
    Optimize product image by resizing and compressing it.
    Returns the product instance with optimized image.
    """
    try:
        if product_instance.image:
            # Open the image
            img = Image.open(product_instance.image)
            
            # Resize image to max width of 600px while maintaining aspect ratio
            max_width = 600
            if img.width > max_width:
                ratio = max_width / img.width
                new_height = int(img.height * ratio)
                img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
            
            # Convert to RGB if necessary (for JPEG compatibility)
            if img.mode in ('RGBA', 'LA', 'P'):
                rgb_img = Image.new('RGB', img.size, (255, 255, 255))
                rgb_img.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = rgb_img
            
            # Save optimized image
            img_io = BytesIO()
            img.save(img_io, 'JPEG', quality=85, optimize=True)
            img_io.seek(0)
            
            # Get the file name and save
            file_name = os.path.splitext(product_instance.image.name)[0] + '_optimized.jpg'
            product_instance.image.save(file_name, ContentFile(img_io.getvalue()), save=False)
    except Exception as e:
        print(f"Error optimizing image for {product_instance.name}: {e}")
    
    return product_instance


def optimize_products_parallel(products):
    """
    Optimize multiple product images in parallel using ThreadPoolExecutor.
    """
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(optimize_product_image, p) for p in products]
        results = [future.result() for future in as_completed(futures)]
    return results


def app(request):
    products = product.objects.all()
    
    # Optimize images in parallel - resizes images to max 600px width
    # and compresses them for faster loading
    if products.exists():
        optimize_products_parallel(list(products))
    
    return render(request, 'newApp/app.html', {'products': products})


def about(request):
    return render(request, 'newApp/about.html')


def contact(request):
    return render(request, 'newApp/contact.html')
