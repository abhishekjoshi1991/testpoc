from webservices import app, sched
# import webservices.schedulers
# from etl.preprocess_wiki_content import PrepareModelDataset
# from webservices.schedulers.preprocess_wiki_content import PrepareModelDataset #working
# from webservices.schedulers.train_model import TrainModel #working

# obj = PrepareModelDataset()
# obj = TrainModel()

port = "7030"
debug = False

if __name__ == "__main__":
    # sched.add_job(id="job1", func=webservices.schedulers.option_chain_scheduler, trigger='interval', minutes=1)
    # sched.add_job(id="job1", func=obj.test_func, trigger='interval', seconds=10)
    # working below
    # sched.add_job(id="job1", func=obj.preprocess_data, trigger='interval', minutes=3)
    # sched.add_job(id="job1", func=obj.train, trigger='interval', minutes=5)
    # sched.start()

    app.run(port=port, debug=debug, use_reloader=False)
    