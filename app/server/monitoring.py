from config import SentrySettings

def enable_sentry(config: SentrySettings) -> None:
    if config.dsn != '':
        import sentry_sdk
        from sentry_sdk.integrations.excepthook import ExcepthookIntegration

        sentry_sdk.init(
            dsn=config.dsn,
            # Set traces_sample_rate to 1.0 to capture 100%
            # of transactions for performance monitoring.
            # We recommend adjusting this value in production.
            traces_sample_rate=config.traces_sample_rate,
            # Configures the sample rate for error events, in the range of 0.0 to 1.0.
            # The default is 1.0 which means that 100% of error events are sent.
            # If set to 0.1 only 10% of error events will be sent. Events are picked randomly.
            sample_rate=config.sample_rate,
            integrations=[
                ExcepthookIntegration(always_run=True),
            ],
            environment=config.env,
            release=config.release,
        )
