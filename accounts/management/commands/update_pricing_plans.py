from django.core.management.base import BaseCommand
from accounts.models import SubscriptionPlan

class Command(BaseCommand):
    help = 'Removes old pricing plans and creates new pricing structure'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('🗑️  Removing old subscription plans...'))
        
        # Delete ALL existing plans
        old_count = SubscriptionPlan.objects.count()
        SubscriptionPlan.objects.all().delete()
        self.stdout.write(
            self.style.SUCCESS(f'✅ Deleted {old_count} old plan(s)')
        )
        
        self.stdout.write(self.style.WARNING('\n📝 Creating new subscription plans...'))
        
        # New pricing plans based on the updated frontend
        plans = [
            {
                'id': 0,
                'name': 'Free Plan',
                'price': 0.00,
                'project_limit': 3,
                'three_d_view_limit': 10,
                'manual_estimate_limit': 3,
                'duration_in_days': 365,  # Free forever (1 year renewal)
            },
            {
                'id': 2,
                'name': 'Starter Plan',
                'price': 19.99,
                'project_limit': 15,
                'three_d_view_limit': 50,
                'manual_estimate_limit': 30,
                'duration_in_days': 30,
            },
            {
                'id': 3,
                'name': 'Pro Plan',
                'price': 49.99,
                'project_limit': 999999,  # Unlimited (very high number)
                'three_d_view_limit': 999999,  # Unlimited 3D views
                'manual_estimate_limit': 999999,  # Unlimited manual estimates
                'duration_in_days': 30,
            },
            {
                'id': 4,
                'name': 'Business Plan',
                'price': 99.99,
                'project_limit': 999999,  # Unlimited
                'three_d_view_limit': 999999,  # Unlimited
                'manual_estimate_limit': 999999,  # Unlimited
                'duration_in_days': 30,
            },
        ]

        for plan_data in plans:
            plan = SubscriptionPlan.objects.create(**plan_data)
            self.stdout.write(
                self.style.SUCCESS(f'✅ Created: {plan.name} - GHS {plan.price}/month')
            )
        
        self.stdout.write(self.style.SUCCESS('\n🎉 All subscription plans updated successfully!'))
        self.stdout.write(self.style.WARNING('\nNew Pricing Structure:'))
        self.stdout.write(self.style.WARNING('━' * 80))
        
        for plan in SubscriptionPlan.objects.all().order_by('price'):
            self.stdout.write(
                f'\n{plan.name}:'
                f'\n  💰 Price: GHS {plan.price}'
                f'\n  📊 Projects: {"Unlimited" if plan.project_limit >= 999999 else plan.project_limit}'
                f'\n  🎨 3D Views: {"Unlimited" if plan.three_d_view_limit >= 999999 else plan.three_d_view_limit}'
                f'\n  📝 Manual Estimates: {"Unlimited" if plan.manual_estimate_limit >= 999999 else plan.manual_estimate_limit}'
                f'\n  ⏰ Duration: {plan.duration_in_days} days'
            )
        
        self.stdout.write(self.style.WARNING('\n' + '━' * 80))
        self.stdout.write(self.style.SUCCESS('\n✨ Database updated! New pricing is ready to use!'))

