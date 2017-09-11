
def get_client_ip(request):
    """

    Function allowing to get user IP address even when IF forwarding is present

    Args:
        request (:obj:`HttpRequest`): the request object, meaning current state of
            variables in a view
    Returns:
        ip address of the client (user, or his internet provider)
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def post(file_path, request, geo_message, location):
    """

    Function that makes the message proper for KML and writes it to file

    Args:
        file_path (str): path to the file, where the data shall be written
        request (:obj:`HttpRequest`): request, requested by users browser to fulfill
        geo_message (str): message, which user wants to deliver
        location (:obj:`tuple` of :obj:`int`): user's location, it's either javascript
            harvested, or when user does not allow, guessed basing on IP adress
            there's no privacy policy on Hoot.

    """
    datas = open(file_path, "r")
    data_tmp = datas.read()[:-27]
    datas.close()
    open('file_path', 'w').close()
    with open(file_path, 'r+') as datas:
        datas.write(data_tmp + '\n\n<Placemark id="' + request.user.username + ', '
                    + strftime("%Y-%m-%d %H:%M:%S", gmtime()) +
                    '">\n\t<name>' + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ': '
                    + request.user.username + ' posts: ' + str(geo_message) +
                    '</name>\n'
                    '\t<magnitude>1.0</magnitude>\n'
                    '\t<Point>\n'
                    '\t\t<coordinates>' + str(float(location[0]) + random() / 10000) + ','
                    + str(float(location[1]) + random() / 10000) +
                    ',0</coordinates>\n'
                    '\t</Point>\n'
                    '</Placemark>'
                    '\n</Folder></Document></kml>')