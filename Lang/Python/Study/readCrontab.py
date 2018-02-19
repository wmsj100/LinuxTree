all = (line for line in open('/etc/crontab', 'r'))
job = (line for line in all)
text = next(job)
print(text)


