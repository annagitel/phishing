    if len(sys.argv) == 4:
        if 'www' in sys.argv[4]:  # url
            try:
                    with urllib.request.urlopen(sys.argv[4]) as f:
                    mail_body = f.read().decode('utf-8')
            except:
                print("failed to read from 4th argument - url")

        elif '.txt' in sys.argv[4]:  # file
            try:
                with open(sys.argv[4], 'r') as file:
                    mail_body = file.read().replace('\n', '')
            except:
                print("failed to read from 4th argument")

        else:  # string
            mail_body = sys.argv[4]

    else:
        mail_body = fill_template(username, job_title)