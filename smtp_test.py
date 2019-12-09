import smtplib

server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
    """To: jcaesar@example.org
    From: soothsayer@example.org

    Beware the Ideas of March.
    """
)

server.quit()