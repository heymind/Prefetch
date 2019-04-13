import os
import pdb
import json
import collections

from itertools import islice

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))
results = []
count = 0
for dirname in os.listdir("."):
    if dirname.startswith("account="):
        count+=1
        for filename in os.listdir(dirname):
            if filename.endswith("crc"):
                continue
            file = open(dirname+"/"+filename, "rb")
            print("=============================================",count)
            print(dirname)
            urls = []
            hosts = []
            for line in file.readlines():
                try:
                    record = json.loads(str(line.decode("utf-8").strip()))
                except Exception as e:
                    print(e)
                urls.append(record["host"] + record["URL"])
                hosts.append(record["host"])
            freq_host = list(reversed(sorted(list(filter(lambda _:_[1]>=2,collections.Counter(hosts).items())))))
            freq_url = list(reversed(sorted(list(filter(lambda _:_[1]>=2,collections.Counter(urls).items())))))
            pdb.set_trace()
            url_vals = list(map(lambda _:_[1],freq_url))
            host_vals = list(map(lambda _:_[1],freq_host))
            Max_url = max(url_values)
            Min_url = min(url_values)
            Avg_url = sum(url_values) / len(url_values)
            Max_host = max(host_vals)
            Min_host = min(host_vals)
            Avg_host = sum(host_vals) / len(host_vals)

            d = dict(
                account=dirname,
                url_freq=take(10,reversed(sorted(dict(freq_url).items()))),
                freq_host=take(10,reversed(sorted(dict(freq_host).items()))),
                max_url=Max_url,
                min_url=Min_host,
                avg_url=Avg_url,
                max_host=Max_host,
                min_host=Min_host,
                avg_host=Avg_host
            )

            results.append(d)
            f = open("result-{}.json".format(count),"w")
            json.dump(d,f)
            f.close()
            f = open("result.json","w")
            json.dump(results,f)
            f.close()
