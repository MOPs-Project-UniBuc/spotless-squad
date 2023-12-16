import time

import sentry_sdk

sentry_sdk.init(
    dsn="https://543eb31bb3cfa5133800e1afad552524@o4506404697210880.ingest.sentry.io/4506404699635712",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
    enable_tracing=True,
)


print("Hello World")

time.sleep(10)

print("Goodbye World")

division_by_zero = 1 / 0
