import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
{
  path: "",
  loadChildren: () => import("./sidebar/sidebar.module").then(m=> m.SidebarModule)
},
{
  path: "**",
  redirectTo: "",
  pathMatch: "full"
}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
