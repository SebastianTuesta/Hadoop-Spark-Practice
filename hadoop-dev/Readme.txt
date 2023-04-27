Count
    cat movie_metadata.csv | python count/mapper.py | sort -k1,1 | python count/reducer.py

    Without Combiner:
        hadoop jar /lib/hadoop/hadoop-streaming.jar \
            -files gs://dataproc-sgtg-input/code/count/mapper.py,gs://dataproc-sgtg-input/code/count/reducer.py \
            -mapper "python3 mapper.py" -reducer "python3 reducer.py" -mapper "python3 reducer.py" \
            -input gs://dataproc-sgtg-input/input/*  \
            -output gs://dataproc-sgtg-input/output

    With combiner:
        hadoop jar /lib/hadoop/hadoop-streaming.jar \
            -files gs://dataproc-sgtg-input/code/count/mapper.py,gs://dataproc-sgtg-input/code/count/reducer.py \
            -mapper "python3 mapper.py" -reducer "python3 reducer.py" -combiner "python3 reducer.py" \
            -input gs://dataproc-sgtg-input/input/* \
            -output gs://dataproc-sgtg-input/output

TOP-k
    cat movie_metadata.csv | python top-k/mapper.py | sort -k1,1 | python top-k/reducer.py

    hadoop jar /lib/hadoop/hadoop-streaming.jar \
            -files gs://dataproc-sgtg-input/code/top-k/mapper.py,gs://dataproc-sgtg-input/code/top-k/reducer.py \
            -mapper "python3 mapper.py" -reducer "python3 reducer.py" -mapper "python3 reducer.py" -combiner "python3 reducer.py" \
            --numReduceTasks 1 \
            -input gs://dataproc-sgtg-input/input/*  \
            -output gs://dataproc-sgtg-input/output
