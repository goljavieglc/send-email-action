import setuptools

with open("DESCRIPTION.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='envio_mail_action',
    version='0.1.0',
    author='Javit0',
    author_email='javi@elgatoylacaja.com',
    description='Esto es un paquete python de prueba',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/goljavi/envio-mail-action',
    license='MIT',
    packages=['envio_mail_action'],
    install_requires=['EmailMessage', 'smtplib'],
)