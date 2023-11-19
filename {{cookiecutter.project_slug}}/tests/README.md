# Test your thing

When your thing does a thing, it better do the *right* thing.

Put whatever testing you feel is appropriate into the tests folder; remember that designing good and effective testing is one of the most beautiful forms of art.

As you introduce inherited and locally packable / testable functionality, try to keep the workflows simple by abstracting the things they do into reusable and testable components in `src`. Each of those should have corresponding tests.

A general guideline for testing, which is enforced by this project.

The *outcome* of workflows should be repeatable and reusable component functionality should be **fully** tested.

Workflows defined within the scope of this thing will be tested automatically.

If you do not specify a testing output the first time you run your tests, it will be generated automatically.

That means that you will *always* pass the first test; your outcome will simply be reused.

Posterior to this your tests will fail when you update source, even when the change is expected. If your internal change results in a completely different answer / expectation, that needs to be a formal change introduced into your data. That change needs to be documented. During the generation of a project the initial test set expectations simply produce an initial workflow outcome and log that locally into a working thing store, clearly marked as 'process output'.

This initial process output may be included as initial test data, simply fill out 'test_cases'.

You may use fixtures to declare elaborate graphs of functionality, dynamically, and collect information about the tests afterwards.

That allows you to build complicated graphs of functionality with a standard interface that are guaranteed to be re-usable, inspectable, and *at minimum* functionally testable.

You will be able to *know* when things are updated in those graphs. You will be able to *know* when updates break things. You will be able to *identify* which change caused the expectation to fail. You will be able to *investigate* the failure in your expectation. You will be able to *isolate* the change in the source which corresponds to the change in expectation by tracing the failure upwards in the graph.

This simply makes things easy on you, by allowing you to say 'generate_expectations'. This will allow you to use *current state of code* to generate *fresh set of expectations*. This effectively resets your data graph by declaring 'current state' should be persisted as the set of expectations. This is useful in a few instances: When you know the code is correct (i.e. simply reusing / wrapping functionality),