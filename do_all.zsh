for i in sorted_list random_no_unique reversed_list random_few_unique; do
    echo running $i;
    python3 perf.py $i
done
