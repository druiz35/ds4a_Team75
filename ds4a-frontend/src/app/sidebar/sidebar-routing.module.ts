import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AboutComponent } from './components/about/about.component';
import { DataDashboardComponent } from './components/data-dashboard/data-dashboard.component';
import { IyrComponent } from './components/iyr/iyr.component';
import { ModelsComponent } from './components/models/models.component';
import { WrapperComponent } from './components/wrapper/wrapper.component';

const routes: Routes = [
{
  path: "",
  component: WrapperComponent,
  children: [
      {
          path: "",
          component: DataDashboardComponent
      },
      {
          path: "data-dashboard", // --> localhost:4200/dashboard
          component: DataDashboardComponent
      },
      {
          path: "acerca",
          component: AboutComponent
      },
      {
          path: "modelos",
          component: ModelsComponent
      },
      {
          path: "iyr",
          component: IyrComponent
      }
  ]
},
{
    path: "**",
    redirectTo: "/data-dashboard",
    pathMatch: "full"
}
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class SidebarRoutingModule { }