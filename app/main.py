"""Main file"""
import os
from http import HTTPStatus
from server import server

SENTRY_DSN = os.getenv("SENTRY_DSN", None)
if SENTRY_DSN is not None:
    import sentry_sdk
    from sentry_sdk.integrations.excepthook import ExcepthookIntegration

    sentry_sdk.init(
        dsn=SENTRY_DSN,
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=float(os.getenv("SENTRY_TRACES_SAMPLE_RATE", 1.0)),
        # Configures the sample rate for error events, in the range of 0.0 to 1.0.
        # The default is 1.0 which means that 100% of error events are sent.
        # If set to 0.1 only 10% of error events will be sent. Events are picked randomly.
        sample_rate=float(os.getenv("SENTRY_SAMPLE_RATE", 1.0)),
        integrations=[
            ExcepthookIntegration(always_run=True),
        ],
        environment=os.getenv("SENTRY_ENV", "production"),
        release=os.getenv("RELEASE_VERSION", "1.0.0"),
    )


@server.get("/", status_code=HTTPStatus.OK)
def root():
    return f"ExtremeCloudIQ & Kadence Integrator"
