from django.core.management.base import BaseCommand
from accounts.models import UserSubscription

class Command(BaseCommand):
    help = 'Fix subscription limits by syncing them with their assigned plan limits'

    def handle(self, *args, **options):
        subscriptions = UserSubscription.objects.all()
        updated_count = 0
        
        for subscription in subscriptions:
            if subscription.plan:
                old_manual_limit = subscription.manual_estimate_limit
                old_project_limit = subscription.project_limit
                old_3d_limit = subscription.three_d_views_limit
                
                subscription.manual_estimate_limit = subscription.plan.manual_estimate_limit
                subscription.project_limit = subscription.plan.project_limit
                subscription.three_d_views_limit = subscription.plan.three_d_view_limit
                subscription.save()
                
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Updated {subscription.user.username}:\n'
                        f'  Manual Estimate: {old_manual_limit} → {subscription.manual_estimate_limit}\n'
                        f'  Projects: {old_project_limit} → {subscription.project_limit}\n'
                        f'  3D Views: {old_3d_limit} → {subscription.three_d_views_limit}'
                    )
                )
                updated_count += 1
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f'Skipped {subscription.user.username}: No plan assigned'
                    )
                )
        
        self.stdout.write(
            self.style.SUCCESS(f'\nSuccessfully updated {updated_count} subscription(s)')
        )
